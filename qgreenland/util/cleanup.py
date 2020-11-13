#!/usr/bin/env python
import os
import shutil
import subprocess
import time

import click

from qgreenland.constants import (INPUT_DIR,
                                  RELEASES_DIR,
                                  TaskType,
                                  WIP_DIR,
                                  ZIP_TRIGGERFILE)

BOOLEAN_CHOICE = click.Choice(['True', 'False'], case_sensitive=False)


def _rmtree(directory, *, retries=3):
    """Add robustness to shutil.rmtree.

    Retries in case of intermittent issues, e.g. with network storage.
    """
    if os.path.isdir(directory):
        for i in range(retries):
            try:
                shutil.rmtree(directory)
                return
            except OSError as e:
                print(f'WARNING: shutil.rmtee failed for path: {directory}')
                print(f'Exception: {e}')
                print(f'Retrying in {i} seconds...')
                time.sleep(i)

        # Allow caller to receive exceptions raised on the final try
        shutil.rmtree(directory)


def cleanup_intermediate_dirs():
    """Delete all intermediate data, except maybe 'fetch' dir."""
    if os.path.isfile(ZIP_TRIGGERFILE):
        os.remove(ZIP_TRIGGERFILE)

    for task_type in TaskType:
        if task_type != TaskType.FETCH:
            _rmtree(task_type.value)

    if os.path.isdir(WIP_DIR):
        for x in os.listdir(WIP_DIR):
            if x.startswith('tmp'):
                _rmtree(x)


def _validate_boolean_choice(_ctx, _param, value):
    if value == 'True':
        return True
    if value == 'False':
        return False

    raise click.BadParameter(
        f'Expected "True" or "False"; Received "{value}"'
    )


def _validate_ambiguous_command(kwargs):
    """Validate for conflicting options and suggest a fix."""
    msg = (
        'Ambiguous command! You have requested both to delete all'
        ' {resource}s _and_ to delete {resource}s by layer ID. Please choose'
        ' only one.'
    )
    if kwargs['layer_id_pattern']:
        if (
            not kwargs['delete_wips_by_pattern']
            and not kwargs['delete_inputs_by_pattern']
        ):
            raise click.UsageError(
                'Ambiguous command! You provided a layer ID glob pattern but'
                ' also requested that no data be deleted by pattern. Please'
                ' either enable deletion of a resource by pattern or remove the'
                ' pattern from your command.'
            )
        if kwargs['delete_all_wip'] and kwargs['delete_wips_by_pattern']:
            raise click.UsageError(msg.format(resource='WIP'))

        if kwargs['delete_all_input'] and kwargs['delete_inputs_by_pattern']:
            raise click.UsageError(msg.format(resource='input'))

    return kwargs


def print_and_run(cmd, *, dry_run):
    print(cmd)
    if not dry_run:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            executable='/bin/bash'  # /bin/sh doesn't support brace expansion
        )


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('dry_run', '--dry-run', '-d',
              help="Print commands, but don't actually delete anything.",
              is_flag=True)
@click.option('delete_inputs_by_pattern', '--delete-inputs-by-pattern', '-i',
              help=(
                  'Use LAYER_ID_PATTERN to delete input-cached layers by glob'
                  ' pattern'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_wips_by_pattern', '--delete-wips-by-pattern', '-w',
              help=(
                  'Use LAYER_ID_PATTERN to delete WIP layers by glob pattern'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='True', show_default=True)
@click.option('delete_all_input', '--delete-all-input', '-I',
              help=(
                  'Delete _ALL_ input-cached layers, ignoring LAYER_ID_PATTERN'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_all_wip', '--delete-all-wip', '-W',
              help=(
                  'Delete _ALL_ WIP layers, ignoring LAYER_ID_PATTERN'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='False', show_default=True)
@click.option('delete_compiled', '--delete-compiled', '-C',
              help=(
                  'Delete compiled (but not zipped) QGreenland datapackage'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='True', show_default=True)
# TODO: delete_all_dev_releases?
@click.option('delete_all_releases', '--delete-all-releases', '-R',
              help=(
                  'Delete all zipped QGreenland releases'
              ),
              type=BOOLEAN_CHOICE, callback=_validate_boolean_choice,
              default='False', show_default=True)
@click.argument('layer_id_pattern',
                required=False, default=None)
# NOTE: Complexity check (C901) is disabled because this function is just a big
#       set of switches by design!
def cleanup_cli(**kwargs):  # noqa: C901
    """Clean up input, WIP, and/or output data created by QGreenland.

    LAYER_ID_PATTERN supports shell globbing (*) and brace expansion to select
    layers to cleanup by id.

    By default, clean up the compiled (but not zipped) datapackage and, if
    LAYER_ID_PATTERN is provided, any matching WIP layers.
    """
    _validate_ambiguous_command(kwargs)

    if kwargs['dry_run']:
        print('WARNING: In DRY RUN mode. Nothing will be deleted.')
        print()

    if kwargs['layer_id_pattern']:
        if kwargs['delete_wips_by_pattern']:
            print_and_run(
                f'rm -rf {TaskType.WIP.value}/{kwargs["layer_id_pattern"]}',
                dry_run=kwargs['dry_run']
            )
        if kwargs['delete_inputs_by_pattern']:
            print_and_run(
                f'rm -rf {INPUT_DIR}/{kwargs["layer_id_pattern"]}',
                dry_run=kwargs['dry_run']
            )

    if kwargs['delete_all_input']:
        print_and_run(
            f'rm -rf {INPUT_DIR}/*',
            dry_run=kwargs['dry_run']
        )

    if kwargs['delete_all_wip']:
        print_and_run(
            f'rm -rf {TaskType.WIP.value}/*',
            dry_run=kwargs['dry_run']
        )

    if kwargs['delete_compiled']:
        print_and_run(
            f'rm -rf {TaskType.FINAL.value}/*',
            dry_run=kwargs['dry_run']
        )
        # The triggerfile tells Luigi tasks to zip the compiled data. Can't do
        # that if we just deleted it!
        if os.path.isfile(ZIP_TRIGGERFILE):
            print_and_run(f'rm {ZIP_TRIGGERFILE}')

    if kwargs['delete_all_releases']:
        print_and_run(
            f'rm -rf {RELEASES_DIR}/*',
            dry_run=kwargs['dry_run']
        )


if __name__ == '__main__':
    cleanup_cli()
