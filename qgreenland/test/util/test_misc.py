import os

from qgreenland.constants import TaskType
from qgreenland.util import misc


def test_layer_fs_path():
    mock_layer_cfg = {
        'id': 'coastlines',
        'group_path': 'group/subgroup',
        'file_type': '.shp'
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
