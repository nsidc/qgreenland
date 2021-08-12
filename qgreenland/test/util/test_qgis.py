import copy
import os
from enum import Enum
from pathlib import Path
from unittest.mock import MagicMock, patch

import qgis.core as qgc

from qgreenland.constants import PACKAGE_DIR
import qgreenland.util.qgis.layer as qgl
import qgreenland.util.qgis.metadata as qgm


test_layers_dir = Path(PACKAGE_DIR) / 'test' / 'data' / 'layers'
class MockTaskType(Enum):
    FINAL = str(test_layers_dir)


@patch(
    'qgreenland.util.misc.TaskType',
    new=MockTaskType,
)
def test_make_map_layer_raster(setup_teardown_qgis_app, raster_layer_cfg):
    result = qgl.make_map_layer(raster_layer_cfg)

    # The result is a a raster layer
    assert isinstance(result, qgc.QgsRasterLayer)

    # Has the expected path to the data on disk.
    expected_raster_path = (
        test_layers_dir / 'group' / 'subgroup' / 'Example raster'
        / 'example.tif'
    )
    assert result.source() == str(expected_raster_path)

    # With the expected shape.
    result_shape = (result.dataProvider().xSize(), result.dataProvider().ySize())
    expected_shape = (2, 2)
    assert result_shape == expected_shape

    # The title is correctly set.
    assert result.name() == raster_layer_cfg.title


def test_make_map_layer_online(setup_teardown_qgis_app, online_layer_cfg):
    result = qgl.make_map_layer(online_layer_cfg)

    assert 'https://demo.mapserver.org' in result.source() 
    assert result.dataProvider().name() == 'wms'
    assert result.name() == online_layer_cfg.title


def test__build_dataset_description(raster_layer_cfg):
    actual = qgm._build_dataset_description(raster_layer_cfg)
    expected = """Example Dataset

Example abstract"""

    assert actual == expected


def __build_dataset_citation(raster_layer_cfg):
    actual = qgm._build_dataset_citation(raster_layer_cfg)
    expected = """Citation:
NSIDC 2020

Citation URL:
https://nsidc.org"""

    assert actual == expected


def test_build_abstract(raster_layer_cfg):
    mock_cfg = copy.deepcopy(raster_layer_cfg)
    actual = qgm.build_layer_abstract(mock_cfg)
    expected = """Example layer description

=== Original Data Source ===
Example Dataset

Example abstract

Citation:
NSIDC 2020

Citation URL:
https://nsidc.org"""

    assert actual == expected
