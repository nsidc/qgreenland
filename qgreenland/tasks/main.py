import os
import shutil

import luigi

from qgreenland import __version__
from qgreenland.constants import DATA_FINAL_DIR, DATA_RELEASE_DIR, TMP_DIR
from qgreenland.tasks.layers import ArcticDEM, BedMachineDataset, Coastlines
from qgreenland.util.file import load_layer_config
from qgreenland.util.misc import make_qgs


class CreateProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        """All layers (not sources) that will be added to the project."""
        yield ArcticDEM()
        yield BedMachineDataset('surface')
        yield BedMachineDataset('thickness')
        yield BedMachineDataset('bed')
        yield Coastlines()

    def output(self):
        return luigi.LocalTarget(f'{TMP_DIR}/READY_TO_ZIP')

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
