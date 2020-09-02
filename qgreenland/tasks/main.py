import os
import shutil

import luigi

from qgreenland import __version__
from qgreenland.constants import (ASSETS_DIR,
                                  CONFIG,
                                  ENVIRONMENT,
                                  PROJECT_DIR,
                                  RELEASE_DIR,
                                  TMP_DIR,
                                  TaskType,
                                  ZIP_TRIGGERFILE)
from qgreenland.util.config import export_config
from qgreenland.util.misc import cleanup_intermediate_dirs
from qgreenland.util.qgis import make_qgis_project_file
from qgreenland.util.task import generate_layer_tasks


class IngestAllLayers(luigi.WrapperTask):
    def requires(self):
        """All layers (not sources) that will be added to the project."""
        # To disable layer(s), edit layers.yml
        tasks = generate_layer_tasks()

        for task in tasks:
            yield task


# TODO: QGreenland{LogoFile, ReadMe, Contributing} are duplicates. DRY/generalize!
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


class LayerManifest(luigi.Task):

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FINAL.value, 'manifest.csv')
        )

    def run(self):
        with self.output().temporary_path() as temp_path:
            export_config(CONFIG, output_path=temp_path)


class QGreenlandReadMe(luigi.Task):

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FINAL.value, 'README.txt')
        )

    def run(self):
        readme = os.path.join(PROJECT_DIR, 'README.md')
        with self.output().temporary_path() as temp_path:
            shutil.copy(readme, temp_path)


class QGreenlandContributing(luigi.Task):

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FINAL.value, 'CONTRIBUTING.txt')
        )

    def run(self):
        readme = os.path.join(PROJECT_DIR, 'CONTRIBUTING.md')
        with self.output().temporary_path() as temp_path:
            shutil.copy(readme, temp_path)


class CreateQgisProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        yield QGreenlandLogoFile()
        yield LayerManifest()
        yield QGreenlandReadMe()
        yield QGreenlandContributing()
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
        fn = f'{RELEASE_DIR}/QGreenland_{__version__}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        tmp_name = f'{TMP_DIR}/final_archive'
        shutil.make_archive(tmp_name, 'zip', TMP_DIR, 'qgreenland')

        os.rename(f'{tmp_name}.zip', self.output().path)

        os.remove(self.input().path)

        if ENVIRONMENT != 'dev':
            cleanup_intermediate_dirs(delete_fetch_dir=False)
