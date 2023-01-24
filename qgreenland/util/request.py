import cgi
import re
import urllib.request
from contextlib import closing
from pathlib import Path

import qgreenland.exceptions as exc
from qgreenland.constants.project import REQUEST_TIMEOUT
from qgreenland.util.edl import create_earthdata_authenticated_session

CHUNK_SIZE = 8 * 1024


# Ignore complexity rule C901
# TODO: make this less complex!
def fetch_and_write_file(  # noqa:C901
    url: str,
    *,
    output_dir: Path,
    session=None,
    verify=True,
):
    """Attempt to download and write file from url.

    Assumes filename from URL or content-disposition header.
    """
    if url.startswith("ftp://"):
        if not verify:
            raise exc.QgrRuntimeError(
                "Ignoring TLS certificate verification is not supported for FTP"
                " sources.",
            )

        _ftp_fetch_and_write(url, output_dir)
    else:
        # TODO: Share the session across requests somehow?
        if not session:
            session = create_earthdata_authenticated_session(hosts=[url], verify=verify)

        with session.get(
            url,
            timeout=REQUEST_TIMEOUT,
            stream=True,
            headers={"User-Agent": "QGreenland"},
        ) as resp:

            # Try to extract the filename from the `content-disposition` header
            if (
                disposition := resp.headers.get("content-disposition")
            ) and "filename" in disposition:
                # Sometimes the filename is quoted, sometimes it's not.
                parsed = cgi.parse_header(disposition)
                # Handle case where disposition itself (usually "attachment")
                # isn't present (geothermal heat flux :bell:).
                matcher = re.compile('filename="?(.*)"?')
                if "filename" in parsed[0] and (match := matcher.match(parsed[0])):
                    fn = match.groups()[0].strip("'\"")
                else:
                    fn = parsed[1]["filename"]
            else:
                if not (fn := _filename_from_url(url)):
                    raise exc.QgrRuntimeError(
                        f"Failed to retrieve output filename from {url}",
                    )

            if resp.status_code != 200:
                raise exc.QgrRuntimeError(
                    f"Received '{resp.status_code}' from {resp.request.url}."
                    f" Content: {resp.text}",
                )

            fp = output_dir / fn

            with open(fp, "wb") as f:
                for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)

        return fp


def _ftp_fetch_and_write(url: str, output_dir: Path) -> None:
    # TODO support earthdata login
    fn = _filename_from_url(url)
    fp = output_dir / fn

    # TODO: do we need `closing`?
    with closing(urllib.request.urlopen(url)) as r:
        with open(fp, "wb") as f:
            while True:
                chunk = r.read(CHUNK_SIZE)
                if not chunk:
                    break
                f.write(chunk)


def _filename_from_url(url: str) -> str:
    url_after_slash_index = url.rfind("/") + 1
    fn = url[url_after_slash_index:]

    if "?" in fn:
        fn = fn.split("?", 1)[0]

    return fn
