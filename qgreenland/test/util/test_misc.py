from pathlib import Path

import pytest

from qgreenland.constants import TaskType
from qgreenland.test.fixtures import raster_layer_cfg as mock_layer_cfg  # noqa: F401
from qgreenland.util import misc


def test_final_layer_dir(mock_layer_cfg):  # noqa: F811
    expected = (
        Path(TaskType.FINAL.value)
        / 'group'
        / 'subgroup'
        / 'Example Raster'
    )

    actual = misc.get_final_layer_dir(mock_layer_cfg)

    assert expected == actual


def test_layer_path_remote():
    layer_cfg = {
        'id': 'coastlines',
        'group_path': 'group/subgroup',
        'file_type': '.shp',
        'source': {
            'urls': ['/vsicurl/http://test.remote.datasource.com']
        },
        'dataset': {
            'access_method': 'gdal_remote'
        }
    }

    expected = '/vsicurl/http://test.remote.datasource.com'

    actual = misc.get_layer_path(layer_cfg)

    assert expected == actual


def test_layer_path_remote_multiple_urls():
    """Multiple URLS are not supported for the `gdal_remote` access method."""
    layer_cfg = {
        'id': 'coastlines',
        'group_path': 'group/subgroup',
        'file_type': '.shp',
        'source': {
            'urls': [
                '/vsicurl/http://test.remote.datasource.com',
                'https://another_url_should_not_be_here.com'
            ]
        },
        'dataset': {
            'access_method': 'gdal_remote'
        }
    }

    with pytest.raises(RuntimeError):
        misc.get_layer_path(layer_cfg)
