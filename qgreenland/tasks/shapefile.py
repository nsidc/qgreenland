import os
import zipfile

import luigi

from qgreenland.constants import TaskType
from qgreenland.tasks.common import FetchData
from qgreenland.util import (LayerConfigMixin,
                             reproject_shapefile,
                             subset_shapefile)


# TODO: Is there any task history? e.g. can we look at the final output target
# and generate a list of tasks that were performed to generate it?
# TODO: s/*Data/*Shapefile/g

class UnzipShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP

    def requires(self):
        return FetchData(self.layer_cfg)

    def output(self):
        of = os.path.join(self.outdir, 'unzipped_filepath.txt')
        return luigi.LocalTarget(of)

    def run(self):
        """Cribbed from.

        https://gist.github.com/miku/2270c2f0d2d11ad1d838
        """
        tmpdir = os.path.join(self.outdir, 'unzip')
        zf = zipfile.ZipFile(self.input().path)

        for fn in zf.namelist():
            if fn.endswith('shp'):
                shp = fn
            zf.extract(fn, tmpdir)
        zf.close()

        with self.output().open('w') as outfile:
            outfile.write(os.path.abspath(os.path.join(tmpdir, shp)))


class ReprojectShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP

    def requires(self):
        return UnzipShapefile(self.layer_cfg)

    def output(self):
        of = os.path.join(self.outdir, 'reprojected_filepath.txt')
        return luigi.LocalTarget(of)

    def run(self):
        tmpfile = os.path.join(self.outdir, 'reproject', 'shapefile.shp')
        with self.input().open('r') as infile:
            shapefile_path = infile.read()

        gdf = reproject_shapefile(shapefile_path)
        os.makedirs(os.path.dirname(tmpfile))
        gdf.to_file(tmpfile, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(tmpfile)


class SubsetShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP

    def requires(self):
        return ReprojectShapefile(self.layer_cfg)

    def output(self):
        of = os.path.join(self.outdir, 'subset_filepath.txt')
        return luigi.LocalTarget(of)

    def run(self):
        tmpfile = os.path.join(self.outdir, 'subset', 'subset.shp')

        with self.input().open('r') as infile:
            reprojected_path = infile.read()

        gdf = subset_shapefile(reprojected_path)
        os.makedirs(os.path.dirname(tmpfile))
        gdf.to_file(tmpfile, driver='ESRI Shapefile')

        with self.output().open('w') as outfile:
            outfile.write(tmpfile)
