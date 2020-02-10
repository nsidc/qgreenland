import os
from contextlib import contextmanager

import yaml

from qgreenland.constants import THIS_DIR


def load_layer_config(layername=None):
    LAYERS_CONFIG = os.path.join(THIS_DIR, 'layers.yml')
    with open(LAYERS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)

    if not layername:
        return config

    # TODO: Add error handling
    try:
        return config[layername]
    except KeyError:
        raise NotImplementedError(
            f"Configuration for layer '{layername}' not found."
        )


def find_shapefile_in_dir(path):
    files = os.listdir(path)
    try:
        f = [x for x in files if x.endswith('.shp')][0]
        return os.path.abspath(os.path.join(path, f))
    except Exception:
        raise RuntimeError(f'No shapefile found in: {files}')


@contextmanager
def temporary_path_dir(target):
    with target.temporary_path() as p:
        try:
            os.makedirs(p, exist_ok=True)
            yield p
        finally:
            pass
    return
