import pytest

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.qgis import setup_qgs_app


@pytest.fixture
def raster_layer_cfg():
    _mock_asset_id = 'only'

    _mock_asset_cfg = {
        'type': 'http',
        'id': _mock_asset_id,
        'urls': ['https://foo.bar.com/data.zip'],
    }

    mock_layer_cfg = ConfigLayer(**{
        'id': 'example_raster',
        'title': 'Example Raster',
        'description': 'Example layer description',
        'hierarchy': ['group', 'subgroup'],
        'input': {
            'dataset': {
                'id': 'example_dataset',
                'assets': {_mock_asset_id: _mock_asset_cfg},
                'metadata': {
                    'title': 'Example Dataset',
                    'abstract': 'Example abstract',
                    'citation': {
                        'text': 'NSIDC 2020',
                        'url': 'https://nsidc.org',
                    },
                },
            },
            'asset': _mock_asset_cfg,
        },
        'steps': [
            {
                'type': 'command',
                'args': ['foo', 'bar'],
            }
        ],
    })

    return mock_layer_cfg


@pytest.fixture(scope='session')
def setup_teardown_qgis_app():
    """Set up and teardown a QgsApplication instance ONCE.

    The QgsApplication must be setup and torn town once (`scope='session'`) and
    only once. Attempting to setup and teardown more than once will result in
    segmentation faults.
    """
    qgs = setup_qgs_app()
    yield qgs
    qgs.exitQgis()
