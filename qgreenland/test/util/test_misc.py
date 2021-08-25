from pathlib import Path

from qgreenland.constants import TaskType
from qgreenland.util import misc


def test_final_layer_dir(raster_layer_node):
    expected = (
        Path(TaskType.FINAL.value)
        / 'Group'
        / 'Subgroup'
        / 'Example raster'
    )

    actual = misc.get_final_layer_dir(raster_layer_node)

    assert expected == actual


def test_vector_or_raster_gdal_remote(online_layer_node):
    assert misc.vector_or_raster(online_layer_node) == 'Raster'
