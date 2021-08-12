# import copy
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import qgis.core as qgc

from qgreenland.constants import PACKAGE_DIR
from qgreenland.util.qgis import layer as qgl

mock_raster_path = Path(PACKAGE_DIR, 'test', 'data', 'example.tif')


@patch(
    'qgreenland.util.qgis.layer.get_final_layer_filepath',
    new=MagicMock(return_value=mock_raster_path),
)
@patch(
    'qgreenland.util.misc.get_final_layer_filepath',
    new=MagicMock(return_value=mock_raster_path),
)
def test_create_raster_map_layer(setup_teardown_qgis_app, raster_layer_cfg):
    result = qgl.make_map_layer(raster_layer_cfg)

    # Assert that the result is a a raster layer
    assert isinstance(result, qgc.QgsRasterLayer)

    # Has the expected path to the data on disk.
    assert result.source() == str(mock_raster_path)

    # With the expected shape.
    result_shape = (result.dataProvider().xSize(), result.dataProvider().ySize())
    expected_shape = (2, 2)
    assert result_shape == expected_shape

    # Assert that the title is correctly set.
    assert result.name() == raster_layer_cfg.title
    assert True

    del result
