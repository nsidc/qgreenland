import glob
import os
import shutil
import time
from contextlib import contextmanager, closing
import urllib.request as request

from qgreenland.constants import (RELEASES_DIR,
                                  REQUEST_TIMEOUT,
                                  TaskType,
                                  WIP_DIR,
                                  ZIP_TRIGGERFILE)
from qgreenland.util.edl import create_earthdata_authenticated_session


def fetch_and_write_file(url, *, output_dir=None, session=None):
    url_slash_index = url.rfind('/')
    fn = url[url_slash_index + 1:]
    fp = os.path.join(output_dir, fn)

    if url.startswith('ftp://'):
        # TODO support earthdata login
        # TODO: do we need `closing`?
        # Stolen from https://stackoverflow.com/questions/11768214/python-download-a-file-from-an-ftp-server
        with closing(request.urlopen(url)) as r:
            with open(fp, 'wb') as f:
                shutil.copyfileobj(r, f)
    else:
        # TODO: Share the session across requests somehow?
        if not session:
            session = create_earthdata_authenticated_session(hosts=[url])

        resp = session.get(url, timeout=REQUEST_TIMEOUT)

        if resp.status_code != 200:
            msg = (f"Received '{resp.status_code}' from {resp.request.url}."
                    f'Content: {resp.text}')
            raise RuntimeError(msg)

        with open(fp, 'wb') as f:
            f.write(resp.content)


def find_in_dir_by_ext(path, *, ext):
    """Find all files in a directory with matching extension.

    Expects an extension with the dot included, e.g. `ext=".shp"`.
    """
    matches = glob.glob(os.path.join(path, '**', f'*{ext}'),
                        recursive=True)

    return [os.path.abspath(os.path.join(path, f)) for f in matches]


def find_single_file_by_ext(path, *, ext):
    """Return a single file with matching extension.

    Fails for any number of results except 1.
    """
    files = find_in_dir_by_ext(path, ext=ext)
    if len(files) > 1:
        raise NotImplementedError(
            "We're not ready to handle multiple '{ext}' files in one task yet!"
        )

    try:
        return files[0]
    except IndexError:
        raise RuntimeError(f"No files with extension '{ext}' found at '{path}'")


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


def get_layer_fn(layer_cfg):
    # NOTE: "file_type" includes a leading period
    return f"{layer_cfg['id']}{layer_cfg['file_type']}"


def get_layer_dir(layer_cfg):
    layer_group_list = layer_cfg.get('group_path', '').split('/')
    return os.path.join(TaskType.FINAL.value,
                        *layer_group_list,
                        layer_cfg['id'])


def get_layer_fs_path(layer_cfg):
    d = get_layer_dir(layer_cfg)
    f = get_layer_fn(layer_cfg)

    return os.path.join(d, f)
