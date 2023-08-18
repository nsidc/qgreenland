# TODO: Move everything in this module into the CLI? I think it makes sense for
# the "dividing line" between Invoke stuff and QGR CLI stuff is "does it _use_
# the QGreenland code" as opposed to "analyzing" it or "exercising" it for
# testing.
import difflib
from pathlib import Path

from invoke import task

from qgreenland.constants.paths import CONFIG_DIR
from qgreenland.util.config.config import get_config, init_config
from qgreenland.util.config.export import export_config_json


@task
def validate(ctx, verbose=False):
    """Validate the configuration files.

    The validation is built-in to the code that loads the config files, and this
    happens when initializing the configuration. Any validation errors will be
    raised from the import statement.
    """
    init_config()
    config = get_config()

    if verbose:
        print("Layers:")
        pprint(config.layers)
        print()
        print("Datasets:")
        pprint(config.datasets)
        print()
        print("Layer Tree:")
        print(config.layer_tree.render())
        print()

    print("🎉🦆 Configuration validation passed.")


@task(aliases=["lock"])
def export(ctx):
    """Export the config as a JSON string."""
    init_config()
    config = get_config()

    print(export_config_json(config))


@task
def diff(ctx):
    """Compare the config lockfile against the current config."""
    init_config()
    config = get_config()

    with open(CONFIG_DIR / "cfg-lock.json", "r") as lockfile:
        # Remove trailing newlines to match `json.dumps` behavior
        lockfile_config = lockfile.read().rstrip("\n")
    current_config = export_config_json(config)

    diff = list(
        difflib.unified_diff(
            lockfile_config.splitlines(keepends=True),
            current_config.splitlines(keepends=True),
            fromfile="lockfile",
            tofile="current_config",
        )
    )

    if len(diff) == 0:
        print("🎉🦆 Configuration comparison passed.")

    else:
        diff_str = "".join(diff)
        raise RuntimeError(
            f"Configuration differs from lockfile:\n{diff_str}\n\n"
            "Please re-export the config (`inv config.export`).",
        )
        ctx.exit(1)
