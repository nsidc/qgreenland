import os
import shutil

import luigi

from qgreenland import __version__
from qgreenland.constants import DATA_FINAL_DIR, DATA_RELEASE_DIR, TMP_DIR
from qgreenland.tasks.layers import ArcticDEM, Coastlines
from qgreenland.util.file import load_layer_config, tempdir_renamed_to
from qgreenland.util.misc import make_qgs


class CreateProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        return [ArcticDEM(), Coastlines()]

    def output(self):
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/qgreenland.qgs')

    def run(self):
        layers_cfg = load_layer_config()

        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        with tempdir_renamed_to(os.path.dirname(self.output().path), act_on_contents=True) as d:
            make_qgs(layers_cfg,
                     self.output().path)


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    def requires(self):
        return CreateProjectFile()

    def output(self):
        os.makedirs(DATA_RELEASE_DIR, exist_ok=True)
        fn = f'{DATA_RELEASE_DIR}/QGreenland_v{__version__}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        tmp_name = f'{TMP_DIR}/final_archive'
        shutil.make_archive(tmp_name, 'zip', TMP_DIR, 'qgreenland')

        os.rename(f'{tmp_name}.zip', self.output().path)
