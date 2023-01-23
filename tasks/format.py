from invoke import task

from .util import PROJECT_DIR, print_and_run


@task(default=True)
def format(ctx):
    """Apply formatting standards to the codebase."""
    # isort 5.10.1 does not support "magic trailing comma" feature of Black, so it will
    # combine multiple imports to one line if they fit.
    #
    #     https://github.com/PyCQA/isort/issues/1683
    print_and_run(f"isort {PROJECT_DIR}")

    # Black 22.1 has problems with string handling. We can work around those with
    # `fmt: on` and `fmt: off` comments, but that's not fun.
    #
    #     https://github.com/psf/black/issues/2188
    print_and_run(f"black {PROJECT_DIR}")
