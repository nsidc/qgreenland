from csv import DictReader

import requests

CMR_CLIENT_ID_HEADER = {'Client-Id': 'nsidc-qgreenland'}
CMR_BASE_URL = 'https://cmr.earthdata.nasa.gov'
CMR_GRANULES_URL = f'{CMR_BASE_URL}/search/granules.csv'

CMR_GRANULES_SCROLL_URL = (
    CMR_GRANULES_URL +
    '?provider=NSIDC_ECS&scroll=true&page_size=2000&'
    'sort_key[]=%2Bstart_date&online_only=true'
)


def granules_from_cmr(short_name, version):
    """Get Granule results from CMR.

    Doesn't support more than one page of results.
    """
    url = (f'{CMR_GRANULES_SCROLL_URL}&short_name={short_name}'
           f'&version={version}')
    resp = requests.get(url, headers=CMR_CLIENT_ID_HEADER)
    if resp.status_code != 200:
        raise RuntimeError(f'Error from CMR: {resp.text}')

    granules = extract_granule_urls_from_cmr_csv(resp.text)

    if len(granules) > 1:
        raise RuntimeError(f'Expected 1 row, got {len(granules)}')

    return granules


def extract_granule_urls_from_cmr_csv(csv):
    # Remove blank lines
    csv = [row for row in csv.split('\n') if row]

    granules = [{k: v for k, v in g.items()}
                for g in DictReader(csv)]

    return granules
