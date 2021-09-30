import logging
import shutil
from abc import ABC
from pathlib import Path

import luigi

from qgreenland.constants import (
    ANCILLARY_DIR,
    ENVIRONMENT,
    PROJECT,
    PROJECT_DIR,
    RELEASES_LAYERS_DIR,
    RELEASE_DIR,
    TMP_DIR,
    TaskType,
    WIP_DIR,
)
from qgreenland.util.cleanup import cleanup_intermediate_dirs
from qgreenland.util.config.config import CONFIG
from qgreenland.util.config.export import export_config_csv, export_config_manifest
from qgreenland.util.luigi import generate_layer_pipelines
from qgreenland.util.qgis.project import (
    QgsApplicationContext,
    make_qgis_project_file,
)
from qgreenland.util.version import get_build_version

logger = logging.getLogger('luigi-interface')


class TaskFilterParams(ABC):
    pattern = luigi.OptionalParameter(default=None)


class IngestAllLayers(luigi.WrapperTask, TaskFilterParams):
    fetch_only = luigi.BoolParameter(default=False)

    def requires(self):
        """All layers (not sources) that will be added to the project."""
        # To disable layer(s), edit layers.yml
        tasks = generate_layer_pipelines(
            pattern=self.pattern,
            fetch_only=self.fetch_only,
        )

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
            TaskType.FINAL.value / self.dest_relative_filepath,
        )

    def run(self):
        with self.output().temporary_path() as temp_path:
            shutil.copy(self.src_filepath, temp_path)


class LayerList(AncillaryFile, TaskFilterParams):
    """A CSV description of layers in the package.

    Intended to be viewed by humans.
    """

    src_filepath = None
    dest_relative_filepath = 'layer_list.csv'

    def requires(self):
        yield IngestAllLayers(pattern=self.pattern)

    def run(self):
        with self.output().temporary_path() as temp_path:
            export_config_csv(CONFIG, output_path=temp_path)


class LayerManifest(luigi.Task, TaskFilterParams):
    """A JSON manifest of layers available for access.

    Intended to be processed by machine, e.g. QGIS plugin.
    """

    def output(self):
        return luigi.LocalTarget(
            RELEASES_LAYERS_DIR / 'manifest.json',
        )

    def requires(self):
        yield IngestAllLayers(pattern=self.pattern)

    def run(self):
        with self.output().temporary_path() as temp_path:
            export_config_manifest(CONFIG, output_path=temp_path)


class CreateQgisProjectFile(luigi.Task, TaskFilterParams):
    """Create .qgz/.qgs project file."""

    def requires(self):
        yield AncillaryFile(
            src_filepath=ANCILLARY_DIR / 'images' / 'qgreenland.png',
            dest_relative_filepath='qgreenland.png',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'README.md',
            dest_relative_filepath='README.txt',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'doc' / 'CONTRIBUTING.md',
            dest_relative_filepath='CONTRIBUTING.txt',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'doc' / 'QuickStartGuide.pdf',
            dest_relative_filepath='QuickStartGuide.pdf',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'doc' / 'UserGuide.pdf',
            dest_relative_filepath='UserGuide.pdf',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'doc' / 'MakingDataQGRCompatible.pdf',
            dest_relative_filepath='MakingDataQGRCompatible.pdf',
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / 'CHANGELOG.md',
            dest_relative_filepath='CHANGELOG.txt',
        )
        yield LayerManifest(pattern=self.pattern)
        yield LayerList(pattern=self.pattern)

    def output(self):
        versioned_package_name = f'{PROJECT}_{get_build_version()}'
        return luigi.LocalTarget(WIP_DIR / versioned_package_name)

    def run(self):
        """Create a symbolic link to trigger the zip."""
        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        with QgsApplicationContext():
            make_qgis_project_file(TaskType.FINAL.value / 'qgreenland.qgs')

        # Create symbolic link to zip with the final versioned filename
        # We don't _need_ a symbolic link here, but this also serves to trigger
        # the next job.
        Path(self.output().path).symlink_to(
            TaskType.FINAL.value,
            target_is_directory=True,
        )


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    def requires(self):
        return CreateQgisProjectFile()

    def output(self):
        RELEASE_DIR.mkdir(parents=True, exist_ok=True)
        fn = f'{RELEASE_DIR}/{PROJECT}_{get_build_version()}.zip'
        return luigi.LocalTarget(fn)

    def run(self):
        logger.info(f'Creating {PROJECT} package: {self.output().path} ...')
        input_path = Path(self.input().path)
        output_path = Path(self.output().path)

        # Create the archive from the symlinked dir.
        tmp_fp = TMP_DIR / 'final_archive.zip'
        tmp_name = f'{tmp_fp.parent}/{tmp_fp.stem}'

        shutil.make_archive(
            tmp_name,
            'zip',
            WIP_DIR,
            input_path.relative_to(WIP_DIR),
        )
        tmp_fp.rename(output_path)

        # Clean up the symlink triggerfile.
        input_path.unlink()

        if ENVIRONMENT != 'dev':
            cleanup_intermediate_dirs()

        # Mathias Nordvig advised the following Greenlandic words:
        """
        For "hooray," the direct Greenlandic translation is simply "horaa!" If
        you want to express that you are shouting "hooray" in the sense of
        celebrating, you can say "horaartorpoq!" A grand celebratory
        expression is a threefold hooray in both Danish and Kalaallisut:
        "Pingasoriarluni horaarutiginninneq!" For "success," you would want to
        say: "Iluatsitsilluarneq!"
        """
        logger.info(
            'Pingasoriarluni horaarutiginninneq!'
            f' Created {PROJECT} package: {output_path}',
        )
