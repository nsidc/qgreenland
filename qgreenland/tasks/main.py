import os
import shutil

import luigi

from qgreenland import PACKAGE_DIR, __version__
from qgreenland.constants import (DATA_FINAL_DIR,
                                  DATA_RELEASE_DIR,
                                  TMP_DIR,
                                  ZIP_TRIGGERFILE)
from qgreenland.tasks.layers import ArcticDEM, BedMachineDataset, Coastlines
from qgreenland.util.misc import load_layer_config
from qgreenland.util.qgis import make_qgs


class QGreenlandLogoFile(luigi.Task):
    """Copy logo file in to the correct location for building the project."""

    def output(self):
        return luigi.LocalTarget(os.path.join(DATA_FINAL_DIR, 'qgreenland.png'))

    def run(self):
        logo = os.path.join(PACKAGE_DIR, 'assets', 'images', 'qgreenland.png')
        with self.output().temporary_path() as temp_path:
            shutil.copy(logo, temp_path)


class CreateProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        """All layers (not sources) that will be added to the project."""
        yield ArcticDEM()
        yield BedMachineDataset('surface')
        yield BedMachineDataset('thickness')
        yield BedMachineDataset('bed')
        yield Coastlines()
        yield QGreenlandLogoFile()

    def output(self):
        return luigi.LocalTarget(ZIP_TRIGGERFILE)

    def run(self):
        layers_cfg = load_layer_config()

        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        make_qgs(layers_cfg,
                 os.path.join(DATA_FINAL_DIR, 'qgreenland.qgs'))

        with self.output().open('w'):
            pass


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

        os.remove(self.input().path)
