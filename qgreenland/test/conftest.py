import pytest

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.qgis.project import QgsApplicationContext

_mock_metadata = {
    'title': 'Example Dataset',
    'abstract': 'Example abstract',
    'citation': {
        'text': 'NSIDC 2020',
        'url': 'https://nsidc.org',
    },
}
_mock_asset_id = 'only'


@pytest.fixture
def online_layer_cfg():
    """Return an example online layer."""
    _mock_online_asset_cfg = {
        'type': 'online',
        'id': _mock_asset_id,
        'provider': 'wms',
        'url': 'crs=EPSG:4326&format=image/png&layers=continents&styles&url=https://demo.mapserver.org/cgi-bin/wms'  # noqa
    }
    return ConfigLayer(**{
        'id': 'example_online',
        'title': 'Example online',
        'description': 'Example layer description',
        'hierarchy': ['foo', 'bar'],
        'input': {
            'dataset': {
                'id': 'baz',
                'assets': {_mock_asset_id: _mock_online_asset_cfg},
                'metadata': _mock_metadata,
            },
            'asset': _mock_online_asset_cfg,
        },
    })


@pytest.fixture
def raster_layer_cfg():
    """Return an example local raster layer."""
    _mock_http_asset_cfg = {
        'type': 'http',
        'id': _mock_asset_id,
        'urls': ['https://foo.bar.com/data.zip'],
    }
    return ConfigLayer(**{
        'id': 'example_raster',
        'title': 'Example raster',
        'description': 'Example layer description',
        'hierarchy': ['group', 'subgroup'],
        'input': {
            'dataset': {
                'id': 'example_dataset',
                'assets': {_mock_asset_id: _mock_http_asset_cfg},
                'metadata': _mock_metadata,
            },
            'asset': _mock_http_asset_cfg,
        },
        'steps': [
            {
                'type': 'command',
                'args': ['foo', 'bar'],
            },
        ],
    })


@pytest.fixture(scope='session')
def setup_teardown_qgis_app():
    """Set up and teardown a QgsApplication instance ONCE.

    The QgsApplication must be setup and torn town once (`scope='session'`) and
    only once. Attempting to setup and teardown more than once will result in
    segmentation faults.
    """
    with QgsApplicationContext():
        yield
