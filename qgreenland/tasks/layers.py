"""layers.py: Top-level tasks for generating layers from dataproducts.

All tasks in this file should read configuration from layers.yml.
"""
import os

import luigi

from qgreenland.constants import DATA_FINAL_DIR
from qgreenland.tasks.raster import SubsetRaster
from qgreenland.tasks.shapefile import SubsetShapefile
from qgreenland.util import load_layer_config, tempdir_renamed_to


# TODO: Consider creating a mixin or something for reading yaml config to
# DRY out the code for layer classes
# e.g. use a class attribute to automatically load config:
#   layername = 'coastlines'
class Coastlines(luigi.Task):
    """Move to final location."""

    layer_name = 'coastlines'
    cfg = load_layer_config(layer_name)

    def requires(self):
        return SubsetShapefile(self.cfg)

    def output(self):
        # TODO: DRY
        parent_dir = self.cfg['layer_group']
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/{parent_dir}/{self.layer_name}/')

    def run(self):
        # TODO: Look at fs.rename_dont_move and do that
        with self.input().open('r') as infile:
            processed_shapefile_path = infile.read()

        processed_shapefile_dir = os.path.dirname(processed_shapefile_path)

        with tempdir_renamed_to(self.output().path) as tempdir:
            for f in os.listdir(processed_shapefile_dir):
                _, ext = f.split('.')
                old_fp = os.path.join(processed_shapefile_dir, f)
                new_fp = os.path.join(
                    tempdir,
                    f'{self.layer_name}.{ext}')

                os.rename(old_fp, new_fp)


class ArcticDEM(luigi.Task):
    """Rename files to their final location."""

    layer_name = 'arctic_dem'
    cfg = load_layer_config(layer_name)

    def requires(self):
        return SubsetRaster(self.cfg)

    def output(self):
        parent_dir = self.cfg['layer_group']

        # TODO should the target be a directory?
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/{parent_dir}/{self.layer_name}/')

    def run(self):
        with tempdir_renamed_to(self.output().path) as tempdir:
            new_fp = os.path.join(
                tempdir,
                f"{self.layer_name}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)
