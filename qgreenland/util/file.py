import os
import pathlib
import stat
import tempfile
from contextlib import contextmanager

import yaml

from qgreenland.constants import THIS_DIR, TMP_DIR


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
def tempdir_renamed_to(target, act_on_contents=False):
    """Write to a temporary directory.

    target: After writing rename to this dir.
    act_on_contents: Rename contents of tempdir inside of target dir instead of
                     renaming the directory itself. Useful for when you want to
                     write arbitrary files to a pre-existing directory.
    """
    d = tempfile.mkdtemp(dir=TMP_DIR)
    try:
        yield d
    finally:
        os.chmod(d,
                 stat.S_IRUSR | stat.S_IXUSR | stat.S_IWUSR |
                 stat.S_IRGRP | stat.S_IXGRP |
                 stat.S_IROTH | stat.S_IXOTH)

        if act_on_contents:
            os.makedirs(pathlib.Path(target), exist_ok=True)
            for f in os.listdir(d):
                os.rename(os.path.join(d, f),
                          os.path.join(target, f))
            os.rmdir(d)
        else:
            os.makedirs(pathlib.Path(target).parent, exist_ok=True)
            os.rename(d, target)
