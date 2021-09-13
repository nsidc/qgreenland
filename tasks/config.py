import difflib
import json
from pathlib import Path
from typing import Any

from invoke import call, task

from qgreenland.constants import CONFIG_DIR


class MagicJSONEncoder(json.JSONEncoder):
      """Call __json__ method of object for JSON serialization.

      Also handle Paths.
      """

      def default(self, o):
          if isinstance(o, Path):
              # Not sure why Paths don't serialize out-of-the-box!
              # https://github.com/samuelcolvin/pydantic/issues/473
              return str(o)
          if hasattr(o, '__json__') and callable(o.__json__):
              return o.__json__()
          return super(MagicJSONEncoder, self).default(o)


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


def _export_json() -> dict[Any, Any]:
    from qgreenland.config import CONFIG
    return json.dumps(CONFIG, cls=MagicJSONEncoder, indent=2, sort_keys=True)


@task
def export(ctx):
    """Export the config as a JSON string."""
    print(_export_json())


@task
def diff(ctx):
    """Compare the config lockfile against the current config."""
    with open(CONFIG_DIR / 'cfg-lock.json', 'r') as lockfile:
        # Remove trailing newlines to match `json.dumps` behavior
        lockfile_config = lockfile.read().rstrip('\n')
    current_config = _export_json()

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
