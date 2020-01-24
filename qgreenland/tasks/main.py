import os
import shutil

import luigi

from qgreenland import __version__
from qgreenland.constants import DATA_FINAL_DIR, DATA_ROOT_DIR
from qgreenland.tasks.layers import Coastlines
from qgreenland.util import make_qgs


class CreateProjectFile(luigi.Task):
    """ Create .qgz/.qgs project file. """
    def requires(self):
        return [Coastlines(), ]

    def output(self):
        return luigi.LocalTarget(f'{DATA_FINAL_DIR}/qgreenland.qgs')

    def run(self):
        make_qgs(self.output().path)


class ZipQGreenland(luigi.Task):
    """ Zip entire QGreenland package for distribution. """
    def requires(self):
        return CreateProjectFile()

    def output(self):
        fn = f'{DATA_ROOT_DIR}/QGreenland_v{__version__}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        tmp_name = f'{DATA_ROOT_DIR}/final_archive'
        shutil.make_archive(tmp_name, 'zip', DATA_ROOT_DIR, 'qgreenland')
        os.rename(f'{tmp_name}.zip', self.output().path)
