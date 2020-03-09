import copy
import os
import shutil
import time
from contextlib import contextmanager

from qgreenland.constants import (CONFIG,
                                  RELEASES_DIR,
                                  REQUEST_TIMEOUT,
                                  TaskType,
                                  WIP_DIR,
                                  ZIP_TRIGGERFILE)
from qgreenland.util.edl import create_earthdata_authenticated_session


def fetch_file(url, *, session=None):
    # TODO: Share the session across requests somehow?
    if not session:
        session = create_earthdata_authenticated_session(hosts=[url])

    return session.get(url, timeout=REQUEST_TIMEOUT)


@contextmanager
def temporary_path_dir(target):
    with target.temporary_path() as p:
        try:
            os.makedirs(p, exist_ok=True)
            yield p
        finally:
            pass
    return


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


def cleanup_output_dirs(delete_fetch_dir=False):
    """Delete all output dirs (intermediate and release).

    WARNING: Should only be called ad-hoc (e.g. cleanup.sh), because this will
    blow away all releases. Defaults to leaving only the 'fetch' dir in place.
    """
    cleanup_intermediate_dirs(delete_fetch_dir=delete_fetch_dir)

    if os.path.isdir(RELEASES_DIR):
        for directory in os.listdir(RELEASES_DIR):
            _rmtree(os.path.join(RELEASES_DIR, directory))


def _find_in_list_by_id(haystack, needle):
    matches = [d for d in haystack if d['id'] == needle]
    if len(matches) > 1:
        raise LookupError(f'Found multiple matches in list with same id: {needle}')

    if len(matches) != 1:
        raise LookupError(f'Found no matches in list with id: {needle}')

    return copy.deepcopy(matches[0])


def get_layer_config(layer_id=None):
    # This import is in a function body because circular import.
    # TODO: Straighten out this spaghetti
    from qgreenland.tasks.layers import INGEST_TASKS

    layers_config = CONFIG['layers']
    datasets_config = CONFIG['datasets']

    for layer_config in layers_config:
        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id, source_id = layer_config['data_source'].split('.')
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['dataset'] = dataset_config

            layer_config['source'] = _find_in_list_by_id(dataset_config['sources'], source_id)
            del layer_config['dataset']['sources']

        # Populate ingest_task with the real function
        if type(layer_config['ingest_task']) is str:
            layer_config['ingest_task'] = INGEST_TASKS[layer_config['ingest_task']]


    if not layer_id:
        return layers_config

    try:
        return _find_in_list_by_id(layers_config, layer_id)
    except LookupError:
        raise NotImplementedError(
            f"Configuration for layer '{layer_id}' not found."
        )


def get_layer_fs_path(layer_name, layer_cfg):
    layer_group_list = layer_cfg.get('path', '').split('/')

    return os.path.join(TaskType.FINAL.value,
                        *layer_group_list,
                        layer_name,
                        f'{layer_name}.{layer_cfg["file_type"]}')
