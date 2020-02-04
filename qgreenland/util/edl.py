import os

import requests

from qgreenland.constants import URS_COOKIE


def create_earthdata_authenticated_session(s=None, *, hosts):
    if not s:
        s = requests.session()

    for host in hosts:
        resp = s.get(host)

        if not (resp.status_code == 401 and 'urs.earthdata.nasa.gov' in resp.url):
            print(f'Host {host} did not redirect to URS -- continuing without auth.')
            return s

        auth_resp = s.get(resp.url, auth=_get_earthdata_creds())
        if not (auth_resp.ok and s.cookies.get(URS_COOKIE) == 'yes'):
            msg = f'Authentication with Earthdata Login failed with:\n{auth_resp.text}'
            raise RuntimeError(msg)

        print(f'Authenticated for {host} with Earthdata Login.')

    return s


def _get_earthdata_creds():
    if not os.environ['EARTHDATA_USERNAME']:
        raise RuntimeError('Environment variable EARTHDATA_USERNAME must be defined.')
    if not os.environ['EARTHDATA_PASSWORD']:
        raise RuntimeError('Environment variable EARTHDATA_PASSWORD must be defined.')

    return (os.environ['EARTHDATA_USERNAME'], os.environ['EARTHDATA_PASSWORD'])
