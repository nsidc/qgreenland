import os
import shutil

import luigi

from qgreenland import __version__
from qgreenland.constants import (ASSETS_DIR,
                                  DATA_RELEASE_DIR,
                                  TMP_DIR,
                                  TaskType,
                                  ZIP_TRIGGERFILE)
from qgreenland.tasks.layers import ArcticDEM, BedMachineDataset, Coastlines
from qgreenland.util.qgis import make_qgs


class QGreenlandLogoFile(luigi.Task):
    """Copy logo file in to the correct location for building the project."""

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FINAL.value, 'qgreenland.png')
        )

    def run(self):
        logo = os.path.join(ASSETS_DIR, 'images', 'qgreenland.png')
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
        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        make_qgs(os.path.join(TaskType.FINAL.value, 'qgreenland.qgs'))

        with self.output().open('w'):
            pass


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    def requires(self):
        return CreateProjectFile()

    def output(self):
        os.makedirs(DATA_RELEASE_DIR, exist_ok=True)
        fn = f'{DATA_RELEASE_DIR}/QGreenland_{__version__}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        tmp_name = f'{TMP_DIR}/final_archive'
        shutil.make_archive(tmp_name, 'zip', TMP_DIR, 'qgreenland')

        os.rename(f'{tmp_name}.zip', self.output().path)

        os.remove(self.input().path)
