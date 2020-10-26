from invoke import task

from qgreenland import __version__
from .util import print_and_run


@task
def bump(ctx, part):
    if part not in ['release', 'minor']:
        print("""
        Until v1.0.0, semver prescribes always incrementing the minor version.
        Use `minor` to increase the minor version and add a "dev" suffix, e.g.:
        v0.19.0 -> v0.20.0dev; use `release` to remove the "dev" suffix, e.g.:
        v0.20.0dev -> v0.20.0.
        """)
        ctx.exit(0)

    if part == 'release' and 'dev' not in __version__:
        raise RuntimeError("Cannot bump version with part 'release': "
                           f'current version is already a release: {__version__}')

    print_and_run(f'bumpversion {part}')
