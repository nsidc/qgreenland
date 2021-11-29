from unittest.mock import patch

import pytest
import qgis.core as qgc

import qgreenland.exceptions as exc
import qgreenland.util.metadata as qgm
import qgreenland.util.qgis.layer as qgl
import qgreenland.util.qgis.project as prj
from qgreenland.test.constants import (
    MOCK_COMPILE_PACKAGE_DIR,
)


def test_make_map_layer_online(setup_teardown_qgis_app, online_layer_node):
    result = qgl.make_map_layer(online_layer_node)

    assert 'https://demo.mapserver.org' in result.source()
    assert result.dataProvider().name() == 'wms'
    assert result.name() == online_layer_node.layer_cfg.title


@patch(
    'qgreenland.util.layer.COMPILE_PACKAGE_DIR',
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test_make_map_layer_raster(setup_teardown_qgis_app, raster_layer_node):
    result = qgl.make_map_layer(raster_layer_node)

    # The result is a a raster layer
    assert isinstance(result, qgc.QgsRasterLayer)

    # Has the expected path to the data on disk.
    expected_raster_path = (
        MOCK_COMPILE_PACKAGE_DIR
        / 'Group' / 'Subgroup'
        / 'Example raster' / 'example.tif'
    )
    assert result.source() == str(expected_raster_path)

    # With the expected shape.
    result_shape = (result.dataProvider().xSize(), result.dataProvider().ySize())
    expected_shape = (2, 2)
    assert result_shape == expected_shape

    # The title is correctly set.
    assert result.name() == raster_layer_node.layer_cfg.title


@patch(
    'qgreenland.util.layer.COMPILE_PACKAGE_DIR',
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test_add_layer_metadata(setup_teardown_qgis_app, raster_layer_node):
    mock_raster_layer = qgl.make_map_layer(raster_layer_node)

    qgl.add_layer_metadata(mock_raster_layer, raster_layer_node.layer_cfg)

    # The abstract gets set with the value returned by `qgis.build_abstract`.
    assert mock_raster_layer.metadata().abstract() == \
        qgm.build_layer_metadata(raster_layer_node.layer_cfg)

    actual_title = mock_raster_layer.metadata().title()
    expected_title = raster_layer_node.layer_cfg.title
    assert actual_title == expected_title

    # Sets the spatial extent based on the the layer extent.
    expected_extent = mock_raster_layer.extent()
    # extent metadata contains both spatial and temporal elements. These are
    # lists. We set one overall extent for the dataset, so take the first element.
    meta_extent = mock_raster_layer.metadata().extent().spatialExtents()[0]
    # The `expected_extent` is a QgsRectangle.
    assert expected_extent == meta_extent.bounds.toRectangle()


@patch(
    'qgreenland.util.layer.COMPILE_PACKAGE_DIR',
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test__add_layers_and_groups(setup_teardown_qgis_app, raster_layer_node):
    # Test that _add_layers_and_groups works without error
    project = qgc.QgsProject.instance()
    prj._add_layers_and_groups(project, raster_layer_node.root)
    added_layers = list(project.mapLayers().values())
    assert len(added_layers) == 1
    assert added_layers[0].name() == 'Example raster'

    # Clear the project for the next test...
    project.clear()

    # Test that an exception is raised when parent groups of a layer are not
    # created first
    with pytest.raises(exc.QgrQgsLayerTreeGroupError):
        prj._add_layers_and_groups(project, raster_layer_node)
    project.clear()
