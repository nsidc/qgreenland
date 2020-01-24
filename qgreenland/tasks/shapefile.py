import os
import zipfile

import luigi

from qgreenland.constants import DATA_WIP_DIR
from qgreenland.tasks.common import FetchData
from qgreenland.util import reproject_shapefile, subset_shapefile


# TODO: Is there any task history? e.g. can we look at the final output target
# and generate a list of tasks that were performed to generate it?
# TODO: s/*Data/*Shapefile/g

class UnzipShapefile(luigi.Task):
    layer_cfg = luigi.Parameter()

    def requires(self):
        return FetchData(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/unzipped_shp_filepath.txt')

    def run(self):
        """Cribbed from.

        https://gist.github.com/miku/2270c2f0d2d11ad1d838
        """
        zf = zipfile.ZipFile(self.input().path)
        unzip_dir = f'{DATA_WIP_DIR}/unzip'

        for fn in zf.namelist():
            if fn.endswith('shp'):
                shp = fn
            zf.extract(fn, unzip_dir)
        zf.close()

        with self.output().open('w') as outfile:
            outfile.write(os.path.abspath(os.path.join(unzip_dir, shp)))


class ReprojectShapefile(luigi.Task):
    layer_cfg = luigi.Parameter()

    def requires(self):
        return UnzipShapefile(self.layer_cfg)

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


class SubsetShapefile(luigi.Task):
    layer_cfg = luigi.Parameter()

    def requires(self):
        return ReprojectShapefile(self.layer_cfg)

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
