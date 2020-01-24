"""layers.py: Top-level tasks for generating layers from dataproducts.

All tasks in this file should read configuration from layers.yml.
"""
import os
import pathlib
import stat
import tempfile

import luigi

from qgreenland.constants import DATA_FINAL_DIR, TMP_DIR
from qgreenland.tasks.shapefile import SubsetShapefile
from qgreenland.util import load_layer_config


class Coastlines(luigi.Task):
    """Move to final location."""
    # TODO: Consider creating a mixin or something for reading yaml config to
    # DRY out the code for layer classes
    # e.g. use a class attribute to automatically load config:
    #   layername = 'coastlines'
    cfg = load_layer_config('coastlines')

    def requires(self):
        return SubsetShapefile(self.cfg)

    def output(self):
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/basemaps/coastlines/')

    def run(self):
        # TODO: Look at fs.rename_dont_move and do that
        with self.input().open('r') as infile:
            processed_shapefile_path = infile.read()

        processed_shapefile_dir = os.path.dirname(processed_shapefile_path)
        temp_shapefile_dir = tempfile.mkdtemp(dir=TMP_DIR)

        # Move and rename each file to temporary location
        for f in os.listdir(processed_shapefile_dir):
            _, ext = f.split('.')
            old_fp = os.path.join(processed_shapefile_dir, f)
            new_fp = os.path.join(temp_shapefile_dir, f'coastlines.{ext}')
            os.rename(old_fp, new_fp)

        # Move temporary files to final location for atomicity
        os.chmod(temp_shapefile_dir,
                 stat.S_IRUSR | stat.S_IXUSR | stat.S_IWUSR |
                 stat.S_IRGRP | stat.S_IXGRP |
                 stat.S_IROTH | stat.S_IXOTH)
        os.makedirs(pathlib.Path(self.output().path).parent)
        os.rename(temp_shapefile_dir, self.output().path)
