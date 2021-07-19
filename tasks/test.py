import sys
from pprint import pprint

from invoke import task

from .util import print_and_run, PROJECT_DIR

sys.path.append(PROJECT_DIR)

from qgreenland.constants import (
    PACKAGE_DIR,
    PROJECT_DIR,
    SCRIPTS_DIR,
    TEST_DIR
)


@task(aliases=['flake8'])
def lint(ctx):
    """Run flake8 linting."""
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' flake8 {PACKAGE_DIR} {SCRIPTS_DIR}',
        pty=True,
    )
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' vulture --min-confidence 100 {PACKAGE_DIR} {SCRIPTS_DIR}',
        pty=True,
    )
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' for file in $(find {SCRIPTS_DIR} -type f -name "*.sh");'
        '    do shellcheck $file;'
        '  done;',
        pty=True,
    )
    print('🎉🙈 Linting passed.')


@task(aliases=['mypy'])
def typecheck(ctx):
    """Run mypy static type analysis."""
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' mypy --config-file={PROJECT_DIR}/.mypy.ini {PACKAGE_DIR} {SCRIPTS_DIR}',
        pty=True,
    )
    print('🎉🦆 Type checking passed.')


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

    print('🎉🦆 Configuration validation passed.')


@task(pre=[lint, typecheck, validate])
def static(ctx):
    """Run static analysis."""
    print(f'🎉🌩️  All static analysis passed.')


@task
def unit(ctx):
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' pytest -c setup.cfg --cov-config=setup.cfg {TEST_DIR}',
        pty=True
    )
    print('🎉🛠️  Unit tests passed.')


@task(pre=[static, unit], default=True)
def all(ctx):
    """Run all tasks."""
    print('🎉❤️  All tests passed!')
