import os
import pathlib
import stat
import tempfile
import zipfile

import luigi

from util import fetch_shapefile_zip, make_qgs, reproject_shapefile, subset_shapefile

# TODO: Figure out a way to use layers.yml or get rid of it

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
LAYER_BASE_DIR = os.path.abspath(os.path.join(THIS_DIR, '../qgis-data/qgreenland/'))
COASTLINE_URL = 'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_coastline.zip'

DATA_ROOT_DIR = '/luigi/data'
DATA_WIP_DIR = f'{DATA_ROOT_DIR}/wip'
DATA_FINAL_DIR = f'{DATA_ROOT_DIR}/qgreenland'

# TODO: Is there any task history? e.g. can we look at the final output target
# and generate a list of tasks that were performed to generate it?
# TODO: s/*Data/*Shapefile/g

class FetchData(luigi.Task):
    def output(self):
        # luigi.format.Nop is required to write binary file.
        # https://github.com/spotify/luigi/issues/1647
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/ne_coastlines.zip',
                                 format=luigi.format.Nop)

    def run(self):
        resp = fetch_shapefile_zip(COASTLINE_URL)
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)


class UnzipData(luigi.Task):
    def requires(self):
        return FetchData()

    def output(self):
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/unzipped_shp_filepath.txt')

    def run(self):
        """ Cribbed from https://gist.github.com/miku/2270c2f0d2d11ad1d838 """
        zf = zipfile.ZipFile(self.input().path)
        unzip_dir = f'{DATA_WIP_DIR}/unzip'

        for fn in zf.namelist():
            if fn.endswith('shp'):
                shp = fn
            zf.extract(fn, unzip_dir)
        zf.close()

        with self.output().open('w') as outfile:
            outfile.write(os.path.abspath(os.path.join(unzip_dir, shp)))


class ReprojectData(luigi.Task):
    def requires(self):
        return UnzipData()

    def output(self):
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/reprojected_shp_filepath.txt')

    def run(self):
        reprojected_fp = os.path.join(f'{DATA_WIP_DIR}/reproject', 'shapefile.shp')

        with self.input().open('r') as infile:
            shapefile_path = infile.read()

        gdf = reproject_shapefile(shapefile_path)
        os.makedirs(os.path.dirname(reprojected_fp))
        gdf.to_file(reprojected_fp, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(reprojected_fp)


class SubsetData(luigi.Task):
    def requires(self):
        return ReprojectData()

    def output(self):
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/subset_shp_filepath.txt')

    def run(self):
        subset_fp = os.path.join(f'{DATA_WIP_DIR}/subset', 'subset.shp')

        with self.input().open('r') as infile:
            reprojected_path = infile.read()

        gdf = subset_shapefile(reprojected_path)
        os.makedirs(os.path.dirname(subset_fp))
        gdf.to_file(subset_fp, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(subset_fp)


class Coastlines(luigi.Task):
    """ Move to final location. """
    def requires(self):
        return SubsetData()

    def output(self):
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/basemaps/coastlines/')

    def run(self):
        # TODO: Look at fs.rename_dont_move and do that
        with self.input().open('r') as infile:
            processed_shapefile_path = infile.read()

        processed_shapefile_dir = os.path.dirname(processed_shapefile_path)
        temp_shapefile_dir = tempfile.mkdtemp(dir='/luigi/data')

        # Move and rename each file to temporary location
        for f in os.listdir(processed_shapefile_dir):
            _, ext = f.split('.')
            old_fp = os.path.join(processed_shapefile_dir, f)
            new_fp = os.path.join(temp_shapefile_dir, f'coastlines.{ext}')
            os.rename(old_fp, new_fp)

        # Move renamed files to final location for atomicity
        # rename_dont_move(temp_shapefile_dir, self.output().path)
        os.chmod(temp_shapefile_dir, stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
        os.makedirs(pathlib.Path(self.output().path).parent)
        os.rename(temp_shapefile_dir, self.output().path)


class CreateProjectFile(luigi.Task):
    """ Create .qgz/.qgs project file. """
    def requires(self):
        return [Coastlines()]

    def output(self):
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/qgreenland.qgs')

    def run(self):
        make_qgs(self.output().path)


class ZipQGreenland(luigi.Task):
    """ Zip entire QGreenland package for distribution. """
    def requires(self):
        # return CreateProjectFile()
        pass
