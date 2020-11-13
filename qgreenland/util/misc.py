import cgi
import glob
import os
import re
import urllib.request
from contextlib import closing, contextmanager

from qgreenland.constants import REQUEST_TIMEOUT, TaskType
from qgreenland.util.edl import create_earthdata_authenticated_session

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


def fetch_and_write_file(url, *, output_dir, session=None):
    """Attempt to download and write file from url.

    Assumes filename from URL or content-disposition header.
    """
    if url.startswith('ftp://'):
        _ftp_fetch_and_write(url, output_dir)
    else:
        # TODO: Share the session across requests somehow?
        if not session:
            session = create_earthdata_authenticated_session(hosts=[url])

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
                        parsed[0]
                    ).groups()[0].strip('\'"')
                else:
                    fn = parsed[1]['filename']
            else:
                if not (fn := _filename_from_url(url)):
                    raise RuntimeError(
                        f'Failed to retrieve output filename from {url}'
                    )

            fp = os.path.join(output_dir, fn)

            if resp.status_code != 200:
                raise RuntimeError(
                    f"Received '{resp.status_code}' from {resp.request.url}."
                    f'Content: {resp.text}'
                )

            with open(fp, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)

        return fp


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
            f"We're not ready to handle multiple '{ext}' files in one task yet!"
        )

    try:
        return files[0]
    except IndexError:
        raise RuntimeError(f"No files with extension '{ext}' found at '{path}'")


@contextmanager
def temporary_path_dir(target):
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


def get_layer_fn(layer_cfg):
    # NOTE: "file_type" includes a leading period
    return f"{layer_cfg['id']}{layer_cfg['file_type']}"


def get_layer_dir(layer_cfg):
    layer_group_list = layer_cfg.get('group_path', '').split('/')
    return os.path.join(TaskType.FINAL.value,
                        *layer_group_list,
                        layer_cfg['id'])


def get_layer_path(layer_cfg):
    if layer_cfg['dataset']['access_method'] == 'gdal_remote':
        if (urls_count := len(layer_cfg['source']['urls'])) != 1:
            raise RuntimeError(
                f"The 'gdal_remote' access method requires 1 URL. Got {urls_count}."
            )

        return f"{layer_cfg['source']['urls'][0]}"

    d = get_layer_dir(layer_cfg)
    f = get_layer_fn(layer_cfg)

    layer_path = os.path.join(d, f)

    if not os.path.isfile(layer_path):
        raise RuntimeError(f"Layer located at '{layer_path}' does not exist.")

    return layer_path
