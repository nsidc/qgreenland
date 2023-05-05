from invoke import call, task

from .util import PROJECT_DIR, print_and_run, rendered_doc_index_file

DOCS_DIR = PROJECT_DIR / "doc"
BUILD_HTML_CMD = "make html"
# SPHINXOPTS default value enables conversion of warnings to errors. We expect there to
# be warnings (specifically, `document isn't included in any toctree`) when building PDF
# docs, since we are excluding contributor docs in that case.
BUILD_PDF_CMD = "make latexpdf SPHINXOPTS=''"


@task
def build_pdf(ctx):
    """Build PDF doc only.

    This is mostly for testing.
    """
    with rendered_doc_index_file(pdf=True):
        print_and_run(
            f"cd {DOCS_DIR} && make clean && {BUILD_PDF_CMD}",
            pty=True,
        )


@task
def build(ctx, pdf=False):
    """Build HTML doc site and optionally PDF as well."""
    print_and_run(
        f"cd {DOCS_DIR} && make clean",
        pty=True,
    )

    with rendered_doc_index_file():
        print_and_run(
            f"cd {DOCS_DIR} && {BUILD_HTML_CMD}",
            pty=True,
        )

    # PDF build happens second, because we expect the HTML build to be
    # warning/error-free. Then the PDF build will have some warnings.
    if pdf:
        with rendered_doc_index_file(pdf=True):
            print_and_run(
                f"cd {DOCS_DIR} && {BUILD_PDF_CMD}",
                pty=True,
            )


@task
def watch(ctx):
    """Build the HTML doc site, and re-build it on each change."""
    script_path = PROJECT_DIR / "scripts" / "experimental" / "build_docs_on_change.sh"

    with rendered_doc_index_file():
        print_and_run(
            str(script_path),
            pty=True,
        )
