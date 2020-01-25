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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        short_name = self.layer_cfg['short_name']
        # TODO: RENAME files to final location instead of writing paths to file
        # TODO: Definitely write a context manager for the above!!!
        self.outfile = f'{DATA_WIP_DIR}/{short_name}/unzipped_filepath.txt'
        self.tmpdir = f'{DATA_WIP_DIR}/{short_name}/unzip'

    def requires(self):
        return FetchData(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(self.outfile)

    def run(self):
        """Cribbed from.

        https://gist.github.com/miku/2270c2f0d2d11ad1d838
        """
        zf = zipfile.ZipFile(self.input().path)

        for fn in zf.namelist():
            if fn.endswith('shp'):
                shp = fn
            zf.extract(fn, self.tmpdir)
        zf.close()

        with self.output().open('w') as outfile:
            outfile.write(os.path.abspath(os.path.join(self.tmpdir, shp)))


class ReprojectShapefile(luigi.Task):
    layer_cfg = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        short_name = self.layer_cfg['short_name']
        self.outfile = f'{DATA_WIP_DIR}/{short_name}/reprojected_filepath.txt'
        self.tmpfile = os.path.join(f'{DATA_WIP_DIR}/{short_name}/reproject',
                                    'shapefile.shp')

    def requires(self):
        return UnzipShapefile(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(self.outfile)

    def run(self):
        with self.input().open('r') as infile:
            shapefile_path = infile.read()

        gdf = reproject_shapefile(shapefile_path)
        os.makedirs(os.path.dirname(self.tmpfile))
        gdf.to_file(self.tmpfile, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(self.tmpfile)


class SubsetShapefile(luigi.Task):
    layer_cfg = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        short_name = self.layer_cfg['short_name']
        self.outfile = f'{DATA_WIP_DIR}/{short_name}/subset_filepath.txt'
        self.tmpfile = os.path.join(f'{DATA_WIP_DIR}/{short_name}/subset',
                                    'subset.shp')

    def requires(self):
        return ReprojectShapefile(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(self.outfile)

    def run(self):
        with self.input().open('r') as infile:
            reprojected_path = infile.read()

        gdf = subset_shapefile(reprojected_path)
        os.makedirs(os.path.dirname(self.tmpfile))
        gdf.to_file(self.tmpfile, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(self.tmpfile)
