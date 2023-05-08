from invoke import call, task

from .util import PROJECT_DIR, print_and_run

DOCS_DIR = PROJECT_DIR / "doc"
CD_AND_CLEAN_CMD = f"cd {DOCS_DIR} && make clean"


@task
def build_pdf(ctx):
    """Build PDF doc only.

    This is mostly for testing.
    """
    # SPHINXOPTS default value enables conversion of warnings to errors. We expect there to
    # be warnings (specifically, `document isn't included in any toctree`) when building PDF
    # docs, since we are excluding contributor docs in that case.
    BUILD_PDF_CMD = f"{CD_AND_CLEAN_CMD} && make latexpdf SPHINXOPTS=''"
    print_and_run(BUILD_PDF_CMD, pty=True)


@task
def build(ctx):
    """Build HTML doc site."""
    BUILD_HTML_CMD = f"{CD_AND_CLEAN_CMD} && make html"
    print_and_run(BUILD_HTML_CMD, pty=True)


@task
def watch(ctx):
    """Build the HTML doc site, and re-build it on each change."""
    script_path = PROJECT_DIR / "scripts" / "experimental" / "build_docs_on_change.sh"
    print_and_run(str(script_path), pty=True)
