import logging
import os
import shutil

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import (ASSETS_DIR,
                                  ENVIRONMENT,
                                  PROJECT_DIR,
                                  RELEASE_DIR,
                                  TMP_DIR,
                                  TaskType,
                                  ZIP_TRIGGERFILE)
from qgreenland.util.config import export_config
from qgreenland.util.cleanup import cleanup_intermediate_dirs
from qgreenland.util.qgis import make_qgis_project_file
from qgreenland.util.task import generate_layer_tasks
from qgreenland.util.version import get_build_version

logger = logging.getLogger('luigi-interface')


class IngestAllLayers(luigi.WrapperTask):
    def requires(self):
        """All layers (not sources) that will be added to the project."""
        # To disable layer(s), edit layers.yml
        tasks = generate_layer_tasks()

        for task in tasks:
            yield task


class AncillaryFile(luigi.Task):
    """Copy an ancillary file in to the final QGreenland package."""

    # Absolute path
    src_filepath = luigi.Parameter()
    # Relative to the root of QGreenland
    dest_relative_filepath = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FINAL.value, self.dest_relative_filepath)
        )

    def run(self):
        with self.output().temporary_path() as temp_path:
            shutil.copy(self.src_filepath, temp_path)


class LayerManifest(AncillaryFile):
    src_filepath = None
    dest_relative_filepath = 'manifest.csv'

    def run(self):
        with self.output().temporary_path() as temp_path:
            export_config(CONFIG, output_path=temp_path)


class CreateQgisProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        yield LayerManifest()
        yield AncillaryFile(
            src_filepath=os.path.join(ASSETS_DIR, 'images', 'qgreenland.png'),
            dest_relative_filepath='qgreenland.png'
        )
        yield AncillaryFile(
            src_filepath=os.path.join(PROJECT_DIR, 'README.md'),
            dest_relative_filepath='README.txt'
        )
        yield AncillaryFile(
            src_filepath=os.path.join(PROJECT_DIR, 'doc', 'CONTRIBUTING.md'),
            dest_relative_filepath='CONTRIBUTING.txt'
        )
        yield AncillaryFile(
            src_filepath=os.path.join(PROJECT_DIR, 'doc', 'STYLE.md'),
            dest_relative_filepath='STYLE.txt'
        )
        yield AncillaryFile(
            src_filepath=os.path.join(PROJECT_DIR, 'CHANGELOG.md'),
            dest_relative_filepath='CHANGELOG.txt'
        )
        yield IngestAllLayers()

    def output(self):
        return luigi.LocalTarget(ZIP_TRIGGERFILE)

    def run(self):
        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        make_qgis_project_file(os.path.join(TaskType.FINAL.value, 'qgreenland.qgs'))

        # Create trigger file and don't write anything
        with self.output().open('w'):
            pass


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    def requires(self):
        return CreateQgisProjectFile()

    def output(self):
        os.makedirs(RELEASE_DIR, exist_ok=True)
        fn = f'{RELEASE_DIR}/QGreenland_{get_build_version()}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        logger.info(f'Creating QGreenland package: {self.output().path} ...')

        tmp_name = f'{TMP_DIR}/final_archive'
        shutil.make_archive(tmp_name, 'zip', TMP_DIR, 'qgreenland')

        os.rename(f'{tmp_name}.zip', self.output().path)

        os.remove(self.input().path)

        if ENVIRONMENT != 'dev':
            cleanup_intermediate_dirs(delete_fetch_dir=False)

        # Mathias Nordvig advised the following Greenlandic words:
        """
        For "hooray," the direct Greenlandic translation is simply "horaa!" If
        you want to express that you are shouting "hooray" in the sense of
        celebrating, you can say "horaartorpoq!" A grand celebratory
        expression is a threefold hooray in both Danish and Kalaallisut:
        "Pingasoriarluni horaarutiginninneq!" For "success," you would want to
        say: "Iluatsitsilluarneq!"
        """
        logger.info('Pingasoriarluni horaarutiginninneq!'
                    f' Created QGreenland package: {self.output().path}')
