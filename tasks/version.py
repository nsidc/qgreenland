from invoke import task

from qgreenland import __version__


@task
def bump(ctx, part):
    if part == 'release' and 'dev' not in __version__:
        raise RuntimeError("Cannot bump version with part 'release': "
                           f'current version is already a release: {__version__}')

    ctx.run(f'bumpversion {part}')
