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
        'title': 'Example Raster'
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
    assert result.name() == mock_layer_cfg['title']


def test__add_layer_metadata():
    mock_raster_path = os.path.join(
        PACKAGE_DIR,
        'test',
        'data',
        'example.tif'
    )

    mock_layer_cfg = {
        'title': 'A very pretty layer',
        'dataset': {
            'metadata': {
                'title': 'Example Dataset',
                'abstract': 'Example abstract',
                'citation': {
                    'text': 'NSIDC 2020',
                    'url': 'https://nsidc.org'
                }
            }
        }
    }

    mock_raster_layer = qgis.create_raster_map_layer(mock_raster_path, mock_layer_cfg)

    qgis._add_layer_metadata(mock_raster_layer, mock_layer_cfg)

    # The abstract gets set with the value returned by `qgis.build_abstract`.
    assert mock_raster_layer.metadata().abstract() == qgis.build_abstract(mock_layer_cfg)

    actual_title = mock_raster_layer.metadata().title()
    expected_title = mock_layer_cfg['title']
    assert actual_title == expected_title

    # Sets the spatial extent based on the the layer extent.
    expected_extent = mock_raster_layer.extent()
    # extent metadata contains both spatial and temporal elements. These are
    # lists. We set one overall extent for the dataset, so take the first element.
    meta_extent = mock_raster_layer.metadata().extent().spatialExtents()[0]
    # The `expected_extent` is a QgsRectangle.
    assert expected_extent == meta_extent.bounds.toRectangle()
