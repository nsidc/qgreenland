from invoke import task

from qgreenland import __version__
from .util import print_and_run


@task
def bump(ctx, part):
    if part == 'release' and 'dev' not in __version__:
        raise RuntimeError("Cannot bump version with part 'release': "
                           f'current version is already a release: {__version__}')

    print_and_run(f'bumpversion {part}')
