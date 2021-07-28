from pathlib import Path
from unittest.mock import patch

import pytest

from qgreenland.constants import TaskType
from qgreenland.util import misc


def test_final_layer_dir():
    mock_layer_cfg = {
        'id': 'coastlines',
        'title': 'Global coastlines',
        'hierarchy': ['group', 'subgroup'],
    }

    expected = (
        Path(TaskType.FINAL.value)
        / 'group'
        / 'subgroup'
        / 'Global coastlines'
    )

    actual = misc.get_final_layer_dir(mock_layer_cfg)

    assert expected == actual


# TODO: Remove xfail once gdal_remote implemented
@pytest.mark.xfail(reason='Remote layers temporarily not imlemented')
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


# TODO: Remove xfail once gdal_remote implemented
@pytest.mark.xfail(reason='Remote layers temporarily not imlemented')
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
