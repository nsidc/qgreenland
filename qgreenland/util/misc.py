import cgi
import glob
import logging
import os
import re
import subprocess
import urllib.request
from contextlib import closing, contextmanager
from pathlib import Path

import luigi

import qgreenland.exceptions as exc
from qgreenland._typing import QgsLayerType
from qgreenland.constants import (
    PROVIDER_LAYERTYPE_MAPPING,
    REQUEST_TIMEOUT,
    TaskType,
)
from qgreenland.models.config.asset import ConfigDatasetOnlineAsset
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.edl import create_earthdata_authenticated_session
from qgreenland.util.tree import LayerNode


logger = logging.getLogger('luigi-interface')
CHUNK_SIZE = 8 * 1024


def _filename_from_url(url):
    url_slash_index = url.rfind('/')
    fn = url[url_slash_index + 1:]

    if '?' in fn:
        fn = fn.split('?', 1)[0]

    return fn


def _ftp_fetch_and_write(url, output_dir):
    # TODO support earthdata login
    fn = _filename_from_url(url)
    fp = os.path.join(output_dir, fn)

    # TODO: do we need `closing`?
    with closing(urllib.request.urlopen(url)) as r:
        with open(fp, 'wb') as f:
            while True:
                chunk = r.read(CHUNK_SIZE)
                if not chunk:
                    break
                f.write(chunk)


# Ignore complexity rule C901
# TODO: make this less complex!
def fetch_and_write_file(url, *, output_dir, session=None, verify=True):  # noqa:C901
    """Attempt to download and write file from url.

    Assumes filename from URL or content-disposition header.
    """
    if url.startswith('ftp://'):
        if not verify:
            raise exc.QgrRuntimeError(
                'Ignoring TLS certificate verification is not supported for FTP'
                ' sources.',
            )

        _ftp_fetch_and_write(url, output_dir)
    else:
        # TODO: Share the session across requests somehow?
        if not session:
            session = create_earthdata_authenticated_session(hosts=[url], verify=verify)

        with session.get(url, timeout=REQUEST_TIMEOUT, stream=True) as resp:

            # Try to extract the filename from the `content-disposition` header
            if (
                (disposition := resp.headers.get('content-disposition'))
                and 'filename' in disposition
            ):
                # Sometimes the filename is quoted, sometimes it's not.
                parsed = cgi.parse_header(disposition)
                # Handle case where disposition itself (usually "attachment")
                # isn't present (geothermal heat flux :bell:).
                if 'filename' in parsed[0]:
                    fn = re.match(
                        'filename="?(.*)"?',
                        parsed[0],
                    ).groups()[0].strip('\'"')
                else:
                    fn = parsed[1]['filename']
            else:
                if not (fn := _filename_from_url(url)):
                    raise exc.QgrRuntimeError(
                        f'Failed to retrieve output filename from {url}',
                    )

            fp = os.path.join(output_dir, fn)

            if resp.status_code != 200:
                raise exc.QgrRuntimeError(
                    f"Received '{resp.status_code}' from {resp.request.url}."
                    f'Content: {resp.text}',
                )

            with open(fp, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)

        return fp


def find_in_dir_by_pattern(path, *, pattern):
    """Find all files in a directory with matching pattern.

    Expects an extension with the dot included, e.g. `pattern=".shp"`.
    """
    matches = glob.glob(os.path.join(path, '**', pattern),
                        recursive=True)

    return [os.path.abspath(os.path.join(path, f)) for f in matches]


def find_single_file_by_name(path, *, filename):
    """Return a single file with matching name.

    Fails for any number of results except 1.
    """
    files = find_in_dir_by_pattern(path, pattern=filename)
    if len(files) > 1:
        raise NotImplementedError(
            f"We're not ready to handle multiple '{filename}' files in one task"
            ' yet!',
        )

    try:
        return files[0]
    except IndexError:
        raise exc.QgrRuntimeError(f"No files with name '{filename}' found at '{path}'")


def find_single_file_by_ext(path, *, ext):
    """Return a single file with matching extension.

    Fails for any number of results except 1.
    """
    files = find_in_dir_by_pattern(path, pattern=f'*{ext}')
    if len(files) > 1:
        raise NotImplementedError(
            f"We're not ready to handle multiple '{ext}' files in one task"
            ' yet!',
        )

    try:
        return files[0]
    except IndexError:
        raise exc.QgrRuntimeError(f"No files with extension '{ext}' found at '{path}'")


# TODO: return a `Path`.
@contextmanager
def temporary_path_dir(target: luigi.Target) -> str:
    """Standardizes Luigi task file output behavior.

    target: a Luigi.FileSystemTarget
            https://luigi.readthedocs.io/en/stable/api/luigi.target.html#luigi.target.FileSystemTarget.temporary_path
    """
    with target.temporary_path() as p:
        try:
            os.makedirs(p, exist_ok=True)
            yield p
        finally:
            pass
    return


def get_layer_fp(layer_dir: Path) -> Path:
    """Look for one and only one standard file type 'gpkg' or 'tif'."""
    # TODO: Extract standard file types into some structure
    rasters = list(layer_dir.glob('*.tif'))
    vectors = list(layer_dir.glob('*.gpkg'))
    files = rasters + vectors

    if len(files) != 1:
        raise exc.QgrRuntimeError(
            'Expected exactly 1 .tif or .gpkg in layer output directory'
            f' {layer_dir}. Found: {files}.',
        )

    return files[0]


def _layer_dirname_from_cfg(layer_cfg: ConfigLayer) -> str:
    return layer_cfg.title


def get_final_layer_dir(
    layer_node: LayerNode,
) -> Path:
    """Get the layer directory in its final pre-zip location."""
    layer_group_path_str = '/'.join(layer_node.group_name_path)
    return (
        Path(TaskType.FINAL.value)
        / layer_group_path_str
        / _layer_dirname_from_cfg(layer_node.layer_cfg)
    )


def get_final_layer_filepath(
    layer_node: LayerNode,
) -> Path:
    d = get_final_layer_dir(layer_node)
    layer_fp = get_layer_fp(d)

    if not layer_fp.is_file():
        raise exc.QgrRuntimeError(f"Layer located at '{layer_fp}' does not exist.")

    return layer_fp


def run_ogr_command(cmd_list):
    cmd = ['.', 'activate', 'gdal', '&&']
    cmd.extend(cmd_list)

    # Hack. The activation of the gdal environment does not work as a list.
    cmd_str = ' '.join(cmd)

    logger.info('Running command:')
    logger.info(cmd_str)
    result = subprocess.run(
        cmd_str,
        shell=True,
        executable='/bin/bash',
        capture_output=True,
    )

    if result.returncode != 0:
        raise exc.QgrRuntimeError(
            str(result.stderr, encoding='utf8'),
        )

    return result


def directory_contents(dir_path: Path) -> list[Path]:
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise exc.QgrRuntimeError(f'`dir_path` must be a directory. Got {dir_path}')

    return sorted(
        dir_path.glob('**/*'),
    )


def directory_size_bytes(dir_path: Path):
    """Return the size of the directory's contents in bytes."""
    contents = directory_contents(dir_path)
    total_size = 0
    for content in contents:
        total_size += content.stat().st_size

    return total_size


def datasource_dirname(*, dataset_id: str, asset_id: str) -> str:
    return f'{dataset_id}.{asset_id}'


def vector_or_raster(layer_node: LayerNode) -> QgsLayerType:
    layer_cfg = layer_node.layer_cfg
    if type(layer_cfg.input.asset) is ConfigDatasetOnlineAsset:
        return PROVIDER_LAYERTYPE_MAPPING[layer_cfg.input.asset.provider]
    else:
        layer_path = get_final_layer_filepath(layer_node)
        return _vector_or_raster_from_fp(layer_path)


def _vector_or_raster_from_fp(fp: Path) -> QgsLayerType:
    if fp.suffix == '.tif':
        return 'Raster'
    elif fp.suffix == '.gpkg':
        return 'Vector'
    else:
        raise exc.QgrQgsLayerError(
            f'Unexpected extension: {fp}. Expected .tif or .gpkg.',
        )
