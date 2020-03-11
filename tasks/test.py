from pprint import pprint

from invoke import task

from .util import print_and_run


@task
def lint(ctx):
    """Run flake8 linting."""
    print_and_run('flake8 .', pty=True)
    print('Linting passed.')


@task
def validate(ctx, verbose=False):
    """Validate the configuration files.

    The validation is built-in to the code that loads the config files, and
    this happens when assigning the CONFIG constant. Any validation errors will
    be raised from the import statement.
    """
    from qgreenland.constants import CONFIG

    if verbose:
        print('Layers:')
        pprint(CONFIG['layers'])
        print('Layer Groups:')
        pprint(CONFIG['layer_groups'])
        print('Datasets:')
        pprint(CONFIG['datasets'])

    print('Configuration is valid.')


@task
def unit(ctx):
    print_and_run('pytest qgreenland/test', pty=True)
    print('Unit tests passed.')


@task(pre=[validate, lint, unit], default=True)
def all(ctx):
    """Run all tasks."""
    pass
