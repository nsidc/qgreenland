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

    assert isinstance(result, qgc.QgsRasterLayer)
