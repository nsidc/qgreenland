from pprint import pprint

from invoke import task

from .util import print_and_run
from qgreenland.constants import PACKAGE_DIR


@task(aliases=['flake8'])
def lint(ctx):
    """Run flake8 linting."""
    print_and_run(f'flake8 {PACKAGE_DIR}', pty=True)
    print_and_run(f'vulture {PACKAGE_DIR} --min-confidence 100', pty=True)
    print('Linting passed.')


@task
def validate(ctx, verbose=False):
    """Validate the configuration files.

    The validation is built-in to the code that loads the config files, and
    this happens when assigning the CONFIG constant. Any validation errors will
    be raised from the import statement.
    """
    from qgreenland.config import CONFIG

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
