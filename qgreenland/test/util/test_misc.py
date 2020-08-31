import os
from unittest.mock import patch

import pytest

from qgreenland.constants import TaskType
from qgreenland.util import misc


@patch('os.path.isfile')
def test_layer_path(mock_isfile):
    mock_isfile.return_value = True

    mock_layer_cfg = {
        'id': 'coastlines',
        'group_path': 'group/subgroup',
        'file_type': '.shp',
        'dataset': {
            'access_method': 'http'
        }
    }

    expected = os.path.join(
        TaskType.FINAL.value,
        'group',
        'subgroup',
        'coastlines',
        'coastlines.shp'
    )

    actual = misc.get_layer_path(mock_layer_cfg)

    assert expected == actual


def test_layer_path_remote():
    mock_layer_cfg = {
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

    actual = misc.get_layer_path(mock_layer_cfg)

    assert expected == actual


def test_layer_path_remote_multiple_urls():
    """Multiple URLS are not supported for the `gdal_remote` access method."""
    mock_layer_cfg = {
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
        misc.get_layer_path(mock_layer_cfg)
