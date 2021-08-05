import pytest

from qgreenland.models.config.layer import ConfigLayer


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
