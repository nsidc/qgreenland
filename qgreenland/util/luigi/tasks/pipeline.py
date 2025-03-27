import logging
import shutil
from pathlib import Path

import luigi

from qgreenland.constants.paths import (
    ANCILLARY_DIR,
    PROJECT_DIR,
    VERSIONED_PACKAGE_DIR,
    WIP_PACKAGE_DIR,
)
from qgreenland.constants.project import ENVIRONMENT, PROJECT
from qgreenland.models.config import Config
from qgreenland.util.cleanup import cleanup_intermediate_dirs
from qgreenland.util.config.config import get_config
from qgreenland.util.config.export import export_config_csv
from qgreenland.util.luigi import generate_layer_pipelines
from qgreenland.util.luigi.tasks.ancillary import (
    AncillaryFile,
    AncillaryMarkdownFileToHtml,
    AncillarySphinxPdfFile,
)
from qgreenland.util.luigi.tasks.main import LinkLayer
from qgreenland.util.misc import compile_package_dir
from qgreenland.util.qgis.project import QgsApplicationContext, make_qgis_project_file
from qgreenland.util.version import get_build_version

logger = logging.getLogger("luigi-interface")


# TODO: Can a wrapper task have Parameters?
class LayersInPackage(luigi.WrapperTask):
    """Hard link layers in to the packaging location."""

    package_name = luigi.Parameter()

    def requires(self):
        tasks = generate_layer_pipelines(package_name=self.package_name)

        for task in tasks:
            yield LinkLayer(
                requires_task=task,
                layer_id=task.layer_cfg.id,
                package_name=self.package_name,
            )


class PackageLayerList(AncillaryFile):
    """A CSV description of layers in the package.

    Intended to be viewed by humans.
    """

    src_filepath = None
    dest_relative_filepath = "layer_list.csv"

    def requires(self):
        yield LayersInPackage(package_name=self.package_name)

    def run(self):
        config = get_config()
        with self.output().temporary_path() as temp_path:
            export_config_csv(
                config,
                output_path=temp_path,
                package_name=self.package_name,
            )


class CreateQgisProjectFile(luigi.Task):
    """Create .qgz/.qgs project file."""

    package_name = luigi.Parameter()

    def requires(self):
        yield LayersInPackage(package_name=self.package_name)
        yield AncillaryFile(
            package_name=self.package_name,
            src_filepath=ANCILLARY_DIR / "images" / "qgreenland.png",
            dest_relative_filepath="qgreenland.png",
        )
        # TODO: Nothing below this line is really _required_ for the project
        # file. Only required for the Zip file. Extract.
        yield AncillaryMarkdownFileToHtml(
            package_name=self.package_name,
            src_filepath=PROJECT_DIR / "README.md",
            dest_relative_filepath="README.html",
        )
        yield AncillaryFile(
            package_name=self.package_name,
            src_filepath=PROJECT_DIR / "doc" / "_pdf" / "QuickStartGuide.pdf",
            dest_relative_filepath="QuickStartGuide.pdf",
        )
        yield AncillaryMarkdownFileToHtml(
            package_name=self.package_name,
            src_filepath=PROJECT_DIR / "CHANGELOG.md",
            dest_relative_filepath="CHANGELOG.html",
        )
        yield AncillarySphinxPdfFile(
            package_name=self.package_name,
            src_filepath=PROJECT_DIR / "doc" / "Makefile",
            dest_relative_filepath="UserGuide.pdf",
        )
        yield PackageLayerList(package_name=self.package_name)

    def output(self):
        versioned_package_name = f"{PROJECT}_{get_build_version()}"
        return luigi.LocalTarget(WIP_PACKAGE_DIR / versioned_package_name)

    def run(self):
        """Create a symbolic link to trigger the zip."""
        # make_qgs outputs multiple files, not just one .qgz file. Similar to
        # writing shapefiles, except this time we want to put them inside a
        # pre-existing directory.
        with QgsApplicationContext():
            make_qgis_project_file(
                compile_package_dir(self.package_name) / "qgreenland.qgz",
                package_name=self.package_name,
            )

        # Create symbolic link to zip with the final versioned filename
        # We don't _need_ a symbolic link here, but this also serves to trigger
        # the next job.
        Path(self.output().path).symlink_to(
            compile_package_dir(self.package_name),
            target_is_directory=True,
        )


class ZipQGreenland(luigi.Task):
    """Zip entire QGreenland package for distribution."""

    package_name = luigi.Parameter()

    def requires(self):
        return CreateQgisProjectFile(package_name=self.package_name)

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


def _unique_packages_in_config(config: Config) -> set[str]:
    packages = set()
    for layer in config.layers.values():
        packages.update(layer.packaging_tags)

    return packages


class QGreenlandPackagesNoZip(luigi.WrapperTask):
    def requires(self):
        config = get_config()
        for package_name in _unique_packages_in_config(config):
            yield CreateQgisProjectFile(package_name=package_name)


class QGreenlandPackages(luigi.WrapperTask):
    def requires(self):
        config = get_config()
        for package_name in _unique_packages_in_config(config):
            yield ZipQGreenland(package_name=package_name)
