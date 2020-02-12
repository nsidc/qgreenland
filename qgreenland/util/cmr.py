import csv
import datetime
import urllib
from collections import namedtuple

import requests

CMR_CLIENT_ID_HEADER = {'Client-Id': 'nsidc-qgreenland'}
CMR_BASE_URL = 'https://cmr.earthdata.nasa.gov'
CMR_GRANULES_URL = f'{CMR_BASE_URL}/search/granules.csv'

CMR_GRANULES_SCROLL_URL = (
    CMR_GRANULES_URL +
    '?provider=NSIDC_ECS&scroll=true&page_size=2000&'
    'sort_key[]=%2Bstart_date&online_only=true'
)

Granule = namedtuple('Granule', ['url', 'start_time'])


class CmrGranules():
    """Modeled after asyncio CmrGranules class in dapaggr.

    TODO:
    - Implement start date and end date parameters.
    - Make a library which provides sync and async versions of this class.

    https://bitbucket.org/nsidc/dapaggr/src/master/dapaggr/cmr.py
    """

    def __init__(self, dataproduct_id, dataproduct_version):
        self.dataproduct_id = dataproduct_id
        self.dataproduct_version = dataproduct_version

        self.http_session = requests.session()
        self.granule_buffer = []  # The remaining granules from the latest fetch
        self.cmr_depleted = False  # We have read all results from CMR

        # Returned on initial query and never changed again:
        self.scroll_id = None  # A unique token for getting the next scroll page
        self.granule_count = None  # Total number of granules CMR has matching this search

        self._init_granules_from_cmr()

    def __len__(self):
        return self.granule_count

    def __iter__(self):
        return self

    def __iterclose__(self):
        return self.http_session.close()

    def __next__(self):
        buffer_depleted = not self.granule_buffer

        if buffer_depleted and not self.cmr_depleted:
            self._next_granules_from_cmr()

        if buffer_depleted and self.cmr_depleted:
            self.__iterclose__()
            raise StopIteration

        # Return from the front of the list (to preserve CMR ordering)
        return self.granule_buffer.pop(0)

    def _next_granules_from_cmr(self):
        headers = CMR_CLIENT_ID_HEADER.copy()
        headers['CMR-Scroll-Id'] = self.scroll_id
        response = self.http_session.get(CMR_GRANULES_URL, headers=headers)

        if not response.ok:
            self.http_session.close()
            raise RuntimeError('Error from CMR: {}'.format(response.text))

        try:
            granules = self._extract_granules(response.text)
        except Exception as e:
            self.http_session.close()
            raise e

        self.granule_buffer.extend(granules)

    def _init_granules_from_cmr(self):
        url = (f'{CMR_GRANULES_SCROLL_URL}'
               f'&short_name={self.dataproduct_id}'
               f'&{self._version_query_string}')
        response = self.http_session.get(url, headers=CMR_CLIENT_ID_HEADER)

        if not response.ok:
            self.http_session.close()
            raise RuntimeError('Error from CMR: {}'.format(response.text))

        self.scroll_id = response.headers['CMR-Scroll-Id']
        self.granule_count = int(response.headers['CMR-Hits'])

        try:
            granules = self._extract_granules(response.text)
        except Exception as e:
            self.http_session.close()
            raise e

        self.granule_buffer.extend(granules)
        self.initialized_cmr_query = True

        if not self.granule_buffer:
            # Got nothing from CMR on initial fetch
            self.cmr_depleted = True

    def _clean_granules_csv(self, granules):
        """Filter out blank lines."""
        return [g for g in granules if g]

    def _extract_granules(self, resp_text):
        granules_csv = self._clean_granules_csv(resp_text.split('\n'))
        granules = [{k: v for k, v in g.items()}
                    for g in csv.DictReader(granules_csv)]

        if not granules:
            self.cmr_depleted = True
            return []

        return [self._normalize_granule(g) for g in granules]

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

        return Granule(url=url, start_time=start_time)

    @property
    def _version_query_string(self):
        max_pad_length = 3
        versions_needed = (max_pad_length - len(str(self.dataproduct_version))) + 1

        versions = ['{pad}{version}'.format(pad='0' * n, version=self.dataproduct_version)
                    for n in range(versions_needed)]
        return '&version={}'.format('&version='.join(versions))
