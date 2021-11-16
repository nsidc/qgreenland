import functools
import subprocess

import click

from qgreenland.constants.paths import (
    COMPILE_PACKAGE_DIR,
    FETCH_DATASETS_DIR,
    RELEASE_LAYERS_DIR,
    RELEASE_PACKAGES_DIR,
    WIP_LAYERS_DIR,
    WIP_PACKAGE_DIR,
)
from qgreenland.util.cli.validate import (
    BOOLEAN_CHOICE,
    # validate_ambiguous_command,
    validate_boolean_choice,
)


def _print_and_run(cmd, *, dry_run):
    print(cmd)
    if not dry_run:
        return subprocess.run(
            cmd,
            shell=True,
            check=True,
            executable='/bin/bash',  # /bin/sh doesn't support brace expansion
        )


@click.command()
@click.option(
    'dry_run', '--dry-run', '-d',
    help='Print commands, but do not actually delete anything',
    is_flag=True,
)
@click.option(
    'dev_run', '--dev', '-D',
    help=(
        'Run a dev cleanup. Includes all package releases, layer releases'
        ' matching PATTERN, package WIP, and layer WIPs matching PATTERN'
    ),
    multiple=True,
    metavar='PATTERN',
)
@click.option(
    'delete_fetch', '--delete-fetch', '-f',
    help=(
        'Delete all fetched datasources, or use PATTERN'
        ' (`{dataset_id}.{asset_id}`) if provided'
    ),
    default='foo',
    # Click v8:
    # is_flag=False, flag_value='foo', default='bar',
    metavar='PATTERN',
)
@click.option(
    'delete_layer_wips_by_pattern', '--delete-layer-wips-by-pattern', '-l',
    help='Delete layer wips by PATTERN (layer ID)',
    multiple=True,
    metavar='PATTERN',
)
@click.option(
    'delete_all_wip', '--delete-all-wip', '-W',
    help='Delete _ALL_ WIP layers, ignoring LAYER_ID_PATTERN',
    type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
    default='False', show_default=True,
)
@click.option(
    'delete_compiled', '--delete-compiled', '-C',
    help='Delete compiled (but not zipped) QGreenland datapackage',
    type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
    default='True', show_default=True,
)
# TODO: delete_all_dev_releases?
@click.option(
    'delete_all_release_packages',
    '--delete-all-release-packages',
    '-R',
    help='Delete all released QGreenland packages',
    type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
    default='False', show_default=True,
)
@click.option(
    'delete_all_dev_release_packages',
    '--delete-all-dev-release-packages',
    '-r',
    help='Delete all released dev QGreenland packages',
    type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
    default='False', show_default=True,
)
@click.option(
    'delete_release_layers_by_pattern',
    '--delete-release-layers-by-pattern',
    '-l',
    help='Pattern used to delete released layers by layer ID',
    multiple=True,
)
@click.option(
    'delete_all_release_layers',
    '--delete-all-release-layers',
    '-L',
    help='Delete all released QGreenland layers',
    type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
    default='False', show_default=True,
)
# NOTE: Complexity check (C901) is disabled because this function is just a big
#       set of switches by design!
def cleanup(**kwargs):  # noqa: C901
    """Clean up input, WIP, and/or output data created by QGreenland.

    By default, clean up the compiled (but not zipped) datapackage.
    """
    breakpoint()
    return
    # validate_ambiguous_command(kwargs)

    if kwargs['dry_run']:
        print('WARNING: In DRY RUN mode. Nothing will be deleted.')
        print()

    print_and_run = functools.partial(_print_and_run, dry_run=kwargs['dry_run'])

    if wip_patterns := kwargs['delete_wips_by_pattern']:
        print_and_run(f'rm -rf {WIP_PACKAGE_DIR}/*')
        for p in wip_patterns:
            print_and_run(f'rm -rf {WIP_LAYERS_DIR}/{p}')

    if kwargs['delete_all_wip']:
        print_and_run(f'rm -rf {WIP_PACKAGE_DIR}/*')
        print_and_run(f'rm -rf {WIP_LAYERS_DIR}/*')

    if inp_patterns := kwargs['delete_fetch_by_pattern']:
        for p in inp_patterns:
            print_and_run(f'rm -rf {FETCH_DATASETS_DIR}/{p}')

    if kwargs['delete_all_fetch']:
        print_and_run(f'rm -rf {FETCH_DATASETS_DIR}/*')

    if kwargs['delete_compiled']:
        print_and_run(f'rm -rf {COMPILE_PACKAGE_DIR}*')

    if kwargs['delete_all_release_packages']:
        print_and_run(f'rm -rf {RELEASE_PACKAGES_DIR}/*')

    if kwargs['delete_all_dev_release_packages']:
        print_and_run(f'rm -rf {RELEASE_PACKAGES_DIR}/dev/*')

    if layer_patterns := kwargs['delete_release_layers_by_pattern']:
        for p in layer_patterns:
            print_and_run(f'rm -rf {RELEASE_LAYERS_DIR}/{p}')

    if kwargs['delete_all_release_layers']:
        print_and_run(f'rm -rf {RELEASE_LAYERS_DIR}/*')


if __name__ == '__main__':
    cleanup()
