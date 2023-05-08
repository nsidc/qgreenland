import logging
import shutil
import tempfile
from pathlib import Path

import luigi
import markdown

from qgreenland.constants.paths import COMPILE_PACKAGE_DIR
from qgreenland.util.command import run_cmd

logger = logging.getLogger("luigi-interface")


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
                        "make",
                        "-C",
                        self.src_filepath.parent,
                        "latexpdf",
                        # Disable the default behavior of converting warnings to errors
                        # TODO: Consider using `invoke` to build the docs?
                        "SPHINXOPTS=''",
                        f"BUILDDIR={build_path}",
                    ]
                )
                output_file = build_path / "latex" / "qgreenland.pdf"
                shutil.copy(output_file, temp_path)

        logger.info(f"Created PDF: {self.output().path}")
