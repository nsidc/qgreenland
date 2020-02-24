import os
import shutil
from contextlib import contextmanager

import yamale

from qgreenland.constants import (CONFIG_DIR,
                                  CONFIG_SCHEMA_DIR,
                                  DATA_DIR,
                                  DATA_RELEASE_DIR,
                                  REQUEST_TIMEOUT,
                                  TaskType,
                                  ZIP_TRIGGERFILE)
from qgreenland.util.edl import create_earthdata_authenticated_session


def fetch_file(url):
    # TODO: Share the session across requests somehow?
    s = create_earthdata_authenticated_session(hosts=[url])

    return s.get(url, timeout=REQUEST_TIMEOUT)


@contextmanager
def temporary_path_dir(target):
    with target.temporary_path() as p:
        try:
            os.makedirs(p, exist_ok=True)
            yield p
        finally:
            pass
    return


def cleanup_output_dirs(delete_fetch_dir=False):
    """Delete output dirs.

    $DATA_DIR/{wip,qgreenland,release,tmp*,READY_TO_ZIP}
    """
    dirs_to_delete = []

    for task_type in TaskType:
        if task_type != TaskType.FETCH or delete_fetch_dir:
            dirs_to_delete.append(
                os.path.join(task_type.value)
            )

    dirs_to_delete.append(DATA_RELEASE_DIR)
    dirs_to_delete.extend(
        [os.path.join(DATA_DIR, x)
         for x in os.listdir(DATA_DIR)
         if x.startswith('tmp')]
    )

    if os.path.isfile(ZIP_TRIGGERFILE):
        os.remove(ZIP_TRIGGERFILE)

    for d in dirs_to_delete:
        if os.path.isdir(d):
            shutil.rmtree(d)


def _load_config(config_filename):
    """Validate config file against schema with Yamale.

    It is expected that the given config filename in CONFIG_DIR has a schema of
    matching name in CONFIG_SCHEMA_DIR.

    Yamale can read in directories of config files, so it returns a list of
    (data, fp) tuples. We always read single files, so we return just the data
    from result[0][0].
    """
    config_fp = os.path.join(CONFIG_DIR, config_filename)
    schema_fp = os.path.join(CONFIG_SCHEMA_DIR, config_filename)

    if not os.path.isfile(config_fp):
        return NotImplementedError(
            'Loading is supported for only one config file at a time.'
        )

    schema = yamale.make_schema(schema_fp)
    config = yamale.make_data(config_fp)
    yamale.validate(schema, config)

    return config[0][0]


def load_layer_config(layername=None):
    config = _load_config('layers.yml')

    if not layername:
        return config

    # TODO: Add error handling
    try:
        return config[layername]
    except KeyError:
        raise NotImplementedError(
            f"Configuration for layer '{layername}' not found."
        )


def load_group_config():
    config = _load_config('layer_groups.yml')

    return config


def get_layer_fs_path(layer_name, layer_cfg):
    layer_group_list = layer_cfg.get('path', '').split('/')

    return os.path.join(TaskType.FINAL.value,
                        *layer_group_list,
                        layer_name,
                        f'{layer_name}.{layer_cfg["file_type"]}')
