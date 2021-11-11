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
    validate_ambiguous_command,
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
@click.option('dry_run', '--dry-run', '-d',
              help="Print commands, but don't actually delete anything.",
              is_flag=True)
@click.option('delete_inputs_by_pattern', '--delete-inputs-by-pattern', '-i',
              help=(
                  'Bash glob/brace pattern used to delete input datasources by'
                  ' `<dataset_id>.<source_id>`'
              ),
              multiple=True)
@click.option('delete_wips_by_pattern', '--delete-wips-by-pattern', '-w',
              help=(
                  'Pattern used to delete WIP layers by layer ID'
              ), multiple=True)
@click.option('delete_all_input', '--delete-all-input', '-I',
              help=(
                  'Delete _ALL_ input-cached layers, ignoring LAYER_ID_PATTERN'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_all_wip', '--delete-all-wip', '-W',
              help=(
                  'Delete _ALL_ WIP layers, ignoring LAYER_ID_PATTERN'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_compiled', '--delete-compiled', '-C',
              help=(
                  'Delete compiled (but not zipped) QGreenland datapackage'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='True', show_default=True)
# TODO: delete_all_dev_releases?
@click.option('delete_all_release_packages',
              '--delete-all-release-packages',
              '-R',
              help=(
                  'Delete all released QGreenland packages'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_all_dev_release_packages',
              '--delete-all-dev-release-packages',
              '-r',
              help=(
                  'Delete all released dev QGreenland packages'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_all_release_layers', '--delete-all-release-layers',
              '-L',
              help=(
                  'Delete all released QGreenland layers'
              ),
              type=BOOLEAN_CHOICE, callback=validate_boolean_choice,
              default='False', show_default=True)
# NOTE: Complexity check (C901) is disabled because this function is just a big
#       set of switches by design!
def cleanup(**kwargs):  # noqa: C901
    """Clean up input, WIP, and/or output data created by QGreenland.

    By default, clean up the compiled (but not zipped) datapackage.
    """
    validate_ambiguous_command(kwargs)

    if kwargs['dry_run']:
        print('WARNING: In DRY RUN mode. Nothing will be deleted.')
        print()

    if wip_patterns := kwargs['delete_wips_by_pattern']:
        _print_and_run(
            f'rm -rf {WIP_PACKAGE_DIR}/*',
            dry_run=kwargs['dry_run'],
        )
        for p in wip_patterns:
            _print_and_run(
                f'rm -rf {WIP_LAYERS_DIR}/{p}',
                dry_run=kwargs['dry_run'],
            )
    if kwargs['delete_all_wip']:
        _print_and_run(
            f'rm -rf {WIP_PACKAGE_DIR}/*',
            dry_run=kwargs['dry_run'],
        )
        _print_and_run(
            f'rm -rf {WIP_LAYERS_DIR}/*',
            dry_run=kwargs['dry_run'],
        )

    if inp_patterns := kwargs['delete_inputs_by_pattern']:
        for p in inp_patterns:
            _print_and_run(
                f'rm -rf {FETCH_DATASETS_DIR}/{p}',
                dry_run=kwargs['dry_run'],
            )
    if kwargs['delete_all_input']:
        _print_and_run(
            f'rm -rf {FETCH_DATASETS_DIR}/*',
            dry_run=kwargs['dry_run'],
        )

    if kwargs['delete_compiled']:
        _print_and_run(
            f'rm -rf {COMPILE_PACKAGE_DIR}*',
            dry_run=kwargs['dry_run'],
        )

    if kwargs['delete_all_release_packages']:
        _print_and_run(
            f'rm -rf {RELEASE_PACKAGES_DIR}/*',
            dry_run=kwargs['dry_run'],
        )

    if kwargs['delete_all_dev_release_packages']:
        _print_and_run(
            f'rm -rf {RELEASE_PACKAGES_DIR}/dev/*',
            dry_run=kwargs['dry_run'],
        )

    if kwargs['delete_all_release_layers']:
        _print_and_run(
            f'rm -rf {RELEASE_LAYERS_DIR}/*',
            dry_run=kwargs['dry_run'],
        )


if __name__ == '__main__':
    cleanup()
