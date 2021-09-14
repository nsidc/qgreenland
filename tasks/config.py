import difflib
from pathlib import Path

from invoke import call, task

from qgreenland.constants import CONFIG_DIR
from qgreenland.util.config import export_config_json


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
        pprint(CONFIG.layers)
        print()
        print('Datasets:')
        pprint(CONFIG.datasets)
        print()
        print('Layer Tree:')
        print(CONFIG.layer_tree.render())
        print()

    print('🎉🦆 Configuration validation passed.')


@task
def export(ctx):
    """Export the config as a JSON string."""
    from qgreenland.config import CONFIG

    print(export_config_json(CONFIG))


@task
def diff(ctx):
    """Compare the config lockfile against the current config."""
    from qgreenland.config import CONFIG

    with open(CONFIG_DIR / 'cfg-lock.json', 'r') as lockfile:
        # Remove trailing newlines to match `json.dumps` behavior
        lockfile_config = lockfile.read().rstrip('\n')
    current_config = export_config_json(CONFIG)

    diff = list(difflib.unified_diff(
        lockfile_config.splitlines(keepends=True),
        current_config.splitlines(keepends=True),
        fromfile='lockfile',
        tofile='current_config',
    ))

    if len(diff) == 0:
        print('🎉🦆 Configuration comparison passed.')

    else:
        diff_str = ''.join(diff)
        raise RuntimeError(
            f'Configuration differs from lockfile:\n{diff_str}\n\n'
            'Please re-export the config (`inv config.export`).',
        )
        ctx.exit(1)
