from pprint import pprint

from invoke import task


@task
def lint(ctx):
    """Run flake8 linting."""
    ctx.run('flake8 .')
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
        pprint(f"{CONFIG['layers']}")
        print('Layer Groups:')
        pprint(f"{CONFIG['layer_groups']}")

    print('Configuration is valid.')


@task(pre=[validate, lint], default=True)
def all(ctx):
    """Run all tasks."""
    pass
