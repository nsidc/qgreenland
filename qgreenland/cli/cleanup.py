import functools
import subprocess

import click

from qgreenland.constants.paths import (
    FETCH_DATASETS_DIR,
    RELEASE_LAYERS_DIR,
    RELEASE_PACKAGES_DIR,
    WIP_LAYERS_DIR,
    WIP_PACKAGE_DIR,
)
from qgreenland.util.cli.validate import validate_ambiguous_command


def _print_and_run(cmd, *, dry_run):
    print(cmd)
    if not dry_run:
        return subprocess.run(
            cmd,
            shell=True,
            check=True,
            # /bin/sh doesn't support brace expansion:
            executable="/bin/bash",
        )


@click.command()
@click.option(
    "dry_run",
    "--dry-run",
    "-d",
    help="Print commands, but do not actually delete anything",
    is_flag=True,
)
@click.option(
    "dev_cleanup",
    "--dev",
    "-D",
    help=(
        "Run a dev cleanup. Includes layer WIPs matching PATTERN, package"
        " WIP, released layers matching PATTERN, and all released packages."
        " If PATTERN is an empty string, no layers will be cleaned up."
    ),
    multiple=True,
    metavar="PATTERN",
)
@click.option(
    "prod_cleanup",
    "--prod",
    "-P",
    help=(
        "Run a prod cleanup. Includes package WIP, all layer WIPs, and all"
        " released layers"
    ),
    is_flag=True,
)
@click.option(
    "delete_all_fetch",
    "--delete-all-fetch",
    "-F",
    help="Delete all fetched dataset assets",
    is_flag=True,
)
@click.option(
    "delete_fetch_by_pattern",
    "--delete-fetch-by-pattern",
    "-f",
    help=(
        "Delete fetched dataset assets matching PATTERN"
        " (`{dataset_id}.{asset_id}`)"  # noqa: FS003
    ),
    multiple=True,
    metavar="PATTERN",
)
@click.option(
    "delete_all_wip_layers",
    "--delete-all-wip-layers",
    "-WL",
    help="Delete all WIP layers",
    is_flag=True,
)
@click.option(
    "delete_wip_layers_by_pattern",
    "--delete-wip-layers-by-pattern",
    "-wl",
    help="Delete WIP layers by PATTERN (layer ID)",
    multiple=True,
    metavar="PATTERN",
)
@click.option(
    "delete_wip_package",
    "--delete-wip-package",
    "-WP",
    help="Delete WIP package",
    is_flag=True,
)
@click.option(
    "delete_all_release_packages",
    "--delete-all-release-packages",
    "-RP",
    help="Delete all released QGreenland packages",
    is_flag=True,
)
@click.option(
    "delete_all_dev_release_packages",
    "--delete-all-dev-release-packages",
    "-rp",
    help="Delete all released dev QGreenland packages",
    is_flag=True,
)
@click.option(
    "delete_all_release_layers",
    "--delete-all-release-layers",
    "-RL",
    help="Delete all released layers",
    is_flag=True,
)
@click.option(
    "delete_release_layers_by_pattern",
    "--delete-release-layers-by-pattern",
    "-rl",
    help="Delete released layers matching PATTERN",
    multiple=True,
    metavar="PATTERN",
)
# NOTE: Complexity check (C901) is disabled because this function is just a big
#       set of switches by design!
def cleanup(**kwargs):  # noqa: C901
    """Clean up input, WIP, and/or output data created by QGreenland.

    By default, clean up the compiled (but not zipped) datapackage.
    """
    validate_ambiguous_command(kwargs)
    if kwargs["dev_cleanup"] and kwargs["prod_cleanup"]:
        raise click.UsageError("Can not do a dev and prod cleanup together.")

    if kwargs["dry_run"]:
        print("WARNING: In DRY RUN mode. Nothing will be deleted.")
        print()
    print_and_run = functools.partial(_print_and_run, dry_run=kwargs["dry_run"])

    if dev_patterns := kwargs["dev_cleanup"]:
        kwargs.update(
            {
                "delete_wip_package": True,
                "delete_all_release_packages": True,
            }
        )
        # Remove empty strings from patterns. You can pass `--dev ''` to only
        # delete packages, not layers.
        dev_patterns = tuple(p for p in dev_patterns if p)
        if dev_patterns:
            kwargs.update(
                {
                    "delete_release_layers_by_pattern": dev_patterns,
                    "delete_wip_layers_by_pattern": dev_patterns,
                }
            )

    elif kwargs["prod_cleanup"]:
        kwargs.update(
            {
                "delete_wip_package": True,
                "delete_all_wip_layers": True,
                "delete_all_release_layers": True,
            }
        )

    # Fetch
    if fetch_patterns := kwargs["delete_fetch_by_pattern"]:
        for p in fetch_patterns:
            print_and_run(f"rm -rf {FETCH_DATASETS_DIR}/{p}")

    if kwargs["delete_all_fetch"]:
        print_and_run(f"rm -rf {FETCH_DATASETS_DIR}/*")

    # WIP
    if wip_patterns := kwargs["delete_wip_layers_by_pattern"]:
        for p in wip_patterns:
            print_and_run(f"rm -rf {WIP_LAYERS_DIR}/{p}")

    if kwargs["delete_all_wip_layers"]:
        print_and_run(f"rm -rf {WIP_LAYERS_DIR}/*")

    if kwargs["delete_wip_package"]:
        print_and_run(f"rm -rf {WIP_PACKAGE_DIR}/*")

    # Release
    if kwargs["delete_all_release_packages"]:
        print_and_run(f"rm -rf {RELEASE_PACKAGES_DIR}/*")

    if kwargs["delete_all_dev_release_packages"]:
        print_and_run(f"rm -rf {RELEASE_PACKAGES_DIR}/dev/*")

    if layer_patterns := kwargs["delete_release_layers_by_pattern"]:
        for p in layer_patterns:
            print_and_run(f"rm -rf {RELEASE_LAYERS_DIR}/{p}")

    if kwargs["delete_all_release_layers"]:
        print_and_run(f"rm -rf {RELEASE_LAYERS_DIR}/*")


if __name__ == "__main__":
    cleanup()
