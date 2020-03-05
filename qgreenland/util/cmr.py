import csv
import datetime
from collections import namedtuple

import requests

from qgreenland.constants import REQUEST_TIMEOUT

CMR_CLIENT_ID_HEADER = {'Client-Id': 'nsidc-qgreenland'}
CMR_BASE_URL = 'https://cmr.earthdata.nasa.gov'
CMR_GRANULES_URL = f'{CMR_BASE_URL}/search/granules.csv'

CMR_GRANULES_SCROLL_URL = (
    CMR_GRANULES_URL +
    '?provider=NSIDC_ECS&scroll=true&page_size=2000&'
    'sort_key[]=%2Bstart_date&online_only=true'
)

Granule = namedtuple('Granule', ['urls', 'start_time'])


def get_cmr_granule(*, granule_ur):
    """Queries CMR for a granule by Granule UR, returns a `Granule`."""

    def _clean_granules_csv(granules):
        """Filter out blank lines."""
        return [g for g in granules if g]

    def _normalize_granule(granule):
        """Create a standardized object from a row extracted from the CMR CSV.

        NOTE: The CSV module uses the first row of the response to get the
        labels. If CMR changes their labels, we will have problems. Same would
        be true if the field order changed, and we have no control over that.
        NOTE: The "Online Access URLs" field can have >1 entry for
        some collections. Currently none of them are implemented.
        """
        url = granule['Online Access URLs']
        start_time = datetime.datetime.strptime(
            granule['Start Time'],
            '%Y-%m-%dT%H:%M:%SZ'
        )

        if not url:
            msg = 'CMR response contains a granule without Online Access URLs: {}'
            raise RuntimeError(msg.format(granule))

        return Granule(urls=tuple(url.split(',')), start_time=start_time)

    def _extract_granule(resp_text):
        granules_csv = _clean_granules_csv(resp_text.split('\n'))

        # We expect a header and just a single data row.
        assert len(granules_csv) == 2
        granule = next(csv.DictReader(granules_csv))

        return _normalize_granule(granule)

    url = (f'{CMR_GRANULES_SCROLL_URL}'
           f'&granule_ur[]={granule_ur}')
    response = requests.get(url,
                            headers=CMR_CLIENT_ID_HEADER,
                            timeout=REQUEST_TIMEOUT)

    if not response.ok:
        raise RuntimeError('Error from CMR: {}'.format(response.text))

    return _extract_granule(response.text)
