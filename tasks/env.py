from invoke import task

from .util import PROJECT_DIR, print_and_run

ENV_LOCKFILE = PROJECT_DIR / "environment.yml"


@task(default=True)
def lock(ctx):
    """Update the `conda-lock.yml` file from the `environment.yml` spec."""
    print_and_run(f"conda-lock -f {ENV_LOCKFILE} -p linux-64")
