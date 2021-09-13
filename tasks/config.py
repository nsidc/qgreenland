import json
from pathlib import Path

from invoke import call, task


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


@task
def export(ctx):
    """Export the config as a JSON string."""
    from qgreenland.config import CONFIG

    the_json = json.dumps(CONFIG, cls=MagicJSONEncoder, indent=2)
    print(the_json)
