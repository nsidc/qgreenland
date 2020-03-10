import os

from qgreenland.constants import TaskType
from qgreenland.util import misc


def test_get_layer_config_all():
    layer_config = misc.get_layer_config()

    # There are at least 2 layers.
    assert len(layer_config.keys()) >= 2


def test_get_layer_config_one():
    # If the layer does not exist, an exception will be raised and pytest will
    # appropriately fail.
    misc.get_layer_config('coastlines')


def test_layer_fs_path():
    mock_layer_cfg = {
        'id': 'coastlines',
        'group_path': 'group/subgroup',
        'file_type': 'shp'
    }

    expected = os.path.join(
        TaskType.FINAL.value,
        'group',
        'subgroup',
        'coastlines',
        'coastlines.shp'
    )

    actual = misc.get_layer_fs_path(mock_layer_cfg)

    assert expected == actual
