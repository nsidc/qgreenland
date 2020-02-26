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


class CmrGranule():
    """Modeled after asyncio CmrGranules class in dapaggr.

    TODO:
    - Implement start date and end date parameters.
    - Make a library which provides sync and async versions of this class.

    https://bitbucket.org/nsidc/dapaggr/src/master/dapaggr/cmr.py

    Note: as of v0.14.0, granule iteration functionality has been stripped out.
    """
    def __init__(self, granule_ur):
        self.granule_ur = granule_ur

        self.http_session = requests.session()

        self.granule = None

    def __call__(self):
        return self._init_granules_from_cmr()

    def _init_granules_from_cmr(self):
        url = (f'{CMR_GRANULES_SCROLL_URL}'
               f'&granule_ur[]={self.granule_ur}')
        response = self.http_session.get(url,
                                         headers=CMR_CLIENT_ID_HEADER,
                                         timeout=REQUEST_TIMEOUT)

        if not response.ok:
            self.http_session.close()
            raise RuntimeError('Error from CMR: {}'.format(response.text))

        try:
            return self._extract_granule(response.text)
        except Exception as e:
            self.http_session.close()
            raise e

    def _clean_granules_csv(self, granules):
        """Filter out blank lines."""
        return [g for g in granules if g]

    def _extract_granule(self, resp_text):
        granules_csv = self._clean_granules_csv(resp_text.split('\n'))

        # We expect a header and just a single data row.
        assert len(granules_csv) == 2
        granule = next(csv.DictReader(granules_csv))

        return self._normalize_granule(granule)

    def _normalize_granule(self, granule):
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

    @property
    def _version_query_string(self):
        max_pad_length = 3
        versions_needed = (max_pad_length - len(str(self.dataproduct_version))) + 1

        versions = ['{pad}{version}'.format(pad='0' * n, version=self.dataproduct_version)
                    for n in range(versions_needed)]
        return '&version={}'.format('&version='.join(versions))
