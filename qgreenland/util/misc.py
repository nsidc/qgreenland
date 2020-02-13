from qgreenland.constants import REQUEST_TIMEOUT
from qgreenland.util.edl import create_earthdata_authenticated_session


def fetch_file(url):
    # TODO: Share the session across requests somehow?
    s = create_earthdata_authenticated_session(hosts=[url])

    return s.get(url, timeout=REQUEST_TIMEOUT)
