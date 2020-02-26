import os

import qgis.core as qgc

from qgreenland.constants import PACKAGE_DIR
from qgreenland.util import qgis


def test_create_raster_map_layer():
    mock_raster_path = os.path.join(
        PACKAGE_DIR,
        'test',
        'data',
        'example.tif'
    )

    mock_layer_cfg = {
        'metadata': {
            'title': 'Example Raster'
        }
    }

    result = qgis.create_raster_map_layer(mock_raster_path, mock_layer_cfg)

    # Assert that the result is a a raster layer
    assert isinstance(result, qgc.QgsRasterLayer)

    # Has the expected path to the data on disk.
    assert result.source() == mock_raster_path

    # With the expected shape.
    result_shape = (result.dataProvider().xSize(), result.dataProvider().ySize())
    expected_shape = (2, 2)
    assert result_shape == expected_shape

    # Assert that the title is correctly set.
    assert result.name() == mock_layer_cfg['metadata']['title']
