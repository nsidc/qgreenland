#!/usr/bin/env python
import os
import shutil
import time

import click

from qgreenland.constants import (INPUT_DIR,
                                  RELEASES_DIR,
                                  REQUEST_TIMEOUT,
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


def cleanup_intermediate_dirs(delete_fetch_dir=False):
    """Delete all intermediate data, except maybe 'fetch' dir."""
    if delete_fetch_dir:
        _rmtree(WIP_DIR)
        return

    if os.path.isfile(ZIP_TRIGGERFILE):
        os.remove(ZIP_TRIGGERFILE)

    for task_type in TaskType:
        if task_type != TaskType.FETCH:
            _rmtree(task_type.value)

    if os.path.isdir(WIP_DIR):
        for x in os.listdir(WIP_DIR):
            if x.startswith('tmp'):
                _rmtree(x)


def _validate_boolean_choice(ctx, param, value):
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


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
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
def cleanup_cli(**kwargs):
    """Cleans up input, WIP, and/or output data created by QGreenland.

    By default, clean up the compiled (but not zipped) datapackage and, if
    LAYER_ID_PATTERN glob pattern is provided, any matching WIP layers.
    """
    _validate_ambiguous_command(kwargs)

    if kwargs['layer_id_pattern']:
        pass

    if kwargs['delete_all_wip']:
        # cleanup_intermediate_dirs(delete_fetch_dir=kwargs['delete_all_input'])
        print(
            'cleanup_intermediate_dirs(delete_fetch_dir='
            f'{kwargs["delete_all_input"]})'
        )

    if kwargs['delete_compiled']:
        return

    if kwargs['delete_all_releases']:
        return

    if kwargs['...']:
        return


if __name__ == '__main__':
    cleanup_cli()
