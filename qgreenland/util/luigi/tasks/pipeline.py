import logging
import shutil
import tempfile
from pathlib import Path

import luigi
import markdown

from qgreenland.constants.paths import (
    ANCILLARY_DIR,
    COMPILE_PACKAGE_DIR,
    PROJECT_DIR,
    RELEASE_LAYERS_DIR,
    VERSIONED_PACKAGE_DIR,
    WIP_PACKAGE_DIR,
)
from qgreenland.constants.project import ENVIRONMENT, PROJECT
from qgreenland.util.cleanup import cleanup_intermediate_dirs
from qgreenland.util.command import run_cmd
from qgreenland.util.config.config import get_config
from qgreenland.util.config.export import export_config_csv, export_config_manifest
from qgreenland.util.luigi import generate_layer_pipelines
from qgreenland.util.luigi.tasks.main import LinkLayer
from qgreenland.util.qgis.project import QgsApplicationContext, make_qgis_project_file
from qgreenland.util.version import get_build_version

logger = logging.getLogger("luigi-interface")


class LayerPipelines(luigi.WrapperTask):
    fetch_only = luigi.BoolParameter(default=False)

    def requires(self):
        """All layers that will be added to the project."""
        tasks = generate_layer_pipelines(
            fetch_only=self.fetch_only,
        )

        for task in tasks:
            yield task


class LayersInPackage(luigi.WrapperTask):
    def requires(self):
        tasks = generate_layer_pipelines()

        for task in tasks:
            if task.layer_cfg.in_package:
                yield LinkLayer(
                    requires_task=task,
                    layer_id=task.layer_cfg.id,
                )


class AncillaryFile(luigi.Task):
    """Copy an ancillary file in to the final QGreenland package."""

    # Absolute path
    src_filepath = luigi.Parameter()
    # Relative to the root of QGreenland
    dest_relative_filepath = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(
            COMPILE_PACKAGE_DIR / self.dest_relative_filepath,
        )

    def run(self):
        with self.output().temporary_path() as temp_path:
            shutil.copy(self.src_filepath, temp_path)


class AncillaryMarkdownFileToHtml(AncillaryFile):
    """Convert an ancillary file to HTML in the final QGreenland package."""

    def run(self):
        with self.output().temporary_path() as temp_path:
            markdown.markdownFromFile(
                input=str(self.src_filepath),
                output=str(temp_path),
            )


class AncillarySphinxPdfFile(AncillaryFile):
    """Generate Sphinx docs as PDF."""

    def run(self):
        with self.output().temporary_path() as temp_path:
            with tempfile.TemporaryDirectory() as build_dir:
                build_path = Path(build_dir)
                run_cmd(
                    [
                        # Run make from the directory containing the Makefile
                        "make",
                        "-C",
                        self.src_filepath.parent,
                        "latexpdf",
                        f"BUILDDIR={build_path}",
                    ]
                )
                output_file = build_path / "latex" / "qgreenland.pdf"
                shutil.copy(output_file, temp_path)

        logger.info(f"Created PDF: {self.output().path}")


class PackageLayerList(AncillaryFile):
    """A CSV description of layers in the package.

    Intended to be viewed by humans.
    """

    src_filepath = None
    dest_relative_filepath = "layer_list.csv"

    def requires(self):
        yield LayersInPackage()

    def run(self):
        config = get_config()
        with self.output().temporary_path() as temp_path:
            export_config_csv(config, output_path=temp_path)


class LayerManifest(luigi.Task):
    """A JSON manifest of layers available for access.

    Intended to be processed by machine, e.g. QGIS plugin.
    """

    def output(self):
        return luigi.LocalTarget(
            RELEASE_LAYERS_DIR / "manifest.json",
        )

    def requires(self):
        yield LayerPipelines()

    def run(self):
        config = get_config()
        with self.output().temporary_path() as temp_path:
            export_config_manifest(config, output_path=temp_path)


class CreateQgisProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    def requires(self):
        yield LayersInPackage()
        yield AncillaryFile(
            src_filepath=ANCILLARY_DIR / "images" / "qgreenland.png",
            dest_relative_filepath="qgreenland.png",
        )
        # TODO: Nothing below this line is really _required_ for the project
        # file. Only required for the Zip file. Extract.
        yield AncillaryMarkdownFileToHtml(
            src_filepath=PROJECT_DIR / "README.md",
            dest_relative_filepath="README.html",
        )
        yield AncillaryFile(
            src_filepath=PROJECT_DIR / "doc" / "_pdf" / "QuickStartGuide.pdf",
            dest_relative_filepath="QuickStartGuide.pdf",
        )
        yield AncillaryMarkdownFileToHtml(
            src_filepath=PROJECT_DIR / "CHANGELOG.md",
            dest_relative_filepath="CHANGELOG.html",
        )
        yield AncillarySphinxPdfFile(
            src_filepath=PROJECT_DIR / "doc" / "Makefile",
            dest_relative_filepath="UserGuide.pdf",
        )
        yield PackageLayerList()

    def output(self):
        versioned_package_name = f"{PROJECT}_{get_build_version()}"
        return luigi.LocalTarget(WIP_PACKAGE_DIR / versioned_package_name)

    def run(self):
        """Create a symbolic link to trigger the zip."""
        # make_qgs outputs multiple files, not just one .qgs file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        with QgsApplicationContext():
            make_qgis_project_file(COMPILE_PACKAGE_DIR / "qgreenland.qgs")

        # Create symbolic link to zip with the final versioned filename
        # We don't _need_ a symbolic link here, but this also serves to trigger
        # the next job.
        Path(self.output().path).symlink_to(
            COMPILE_PACKAGE_DIR,
            target_is_directory=True,
        )


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    def requires(self):
        return CreateQgisProjectFile()

    def output(self):
        VERSIONED_PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
        fn = f"{VERSIONED_PACKAGE_DIR}/{PROJECT}_{get_build_version()}.zip"
        return luigi.LocalTarget(fn)

    def run(self):
        logger.info(f"Creating {PROJECT} package: {self.output().path} ...")
        input_path = Path(self.input().path)
        output_path = Path(self.output().path)

        # Create the archive from the symlinked dir.
        tmp_fp = WIP_PACKAGE_DIR / "final_archive.zip"
        shutil.make_archive(
            # make_archive expects a file path without extension:
            f"{tmp_fp.parent}/{tmp_fp.stem}",
            format="zip",
            root_dir=WIP_PACKAGE_DIR,
            base_dir=input_path.relative_to(WIP_PACKAGE_DIR),
        )
        tmp_fp.rename(output_path)

        # Clean up the symlink triggerfile.
        input_path.unlink()

        if ENVIRONMENT != "dev":
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
            "Pingasoriarluni horaarutiginninneq!"
            f" Created {PROJECT} package: {output_path}",
        )


class HostedLayers(luigi.WrapperTask):
    def requires(self):
        yield LayerPipelines()
        yield LayerManifest()


class QGreenlandAll(luigi.WrapperTask):
    def requires(self):
        yield ZipQGreenland()
        yield HostedLayers()


class QGreenlandNoZip(luigi.WrapperTask):
    def requires(self):
        yield CreateQgisProjectFile()
        yield HostedLayers()
