# import copy
import os
from enum import Enum
from pathlib import Path
from unittest.mock import MagicMock, patch

import qgis.core as qgc

from qgreenland.constants import PACKAGE_DIR
from qgreenland.util.qgis import layer as qgl

test_layers_dir = Path(PACKAGE_DIR) / 'test' / 'data' / 'layers'
class MockTaskType(Enum):
    FINAL = str(test_layers_dir)


@patch(
    'qgreenland.util.misc.TaskType',
    new=MockTaskType,
)
def test_create_raster_map_layer(setup_teardown_qgis_app, raster_layer_cfg):
    result = qgl.make_map_layer(raster_layer_cfg)

    # Assert that the result is a a raster layer
    assert isinstance(result, qgc.QgsRasterLayer)

    # Has the expected path to the data on disk.
    expected_raster_path = test_layers_dir / 'group' / 'subgroup' / 'example.tif'
    assert result.source() == str(expected_raster_path)

    # With the expected shape.
    result_shape = (result.dataProvider().xSize(), result.dataProvider().ySize())
    expected_shape = (2, 2)
    assert result_shape == expected_shape

    # Assert that the title is correctly set.
    assert result.name() == raster_layer_cfg.title
    assert True

    del result
