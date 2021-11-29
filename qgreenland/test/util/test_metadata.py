import copy

import qgreenland.util.metadata as qgm


def test__build_dataset_description(raster_layer_cfg):
    actual = qgm._build_dataset_description(raster_layer_cfg)
    expected = """Example Dataset

Example abstract."""

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
    actual = qgm.build_layer_metadata(mock_cfg)
    expected = """Example layer description.

=== Original Data Source ===
Example Dataset

Example abstract.

Citation:
NSIDC 2020

Citation URL:
https://nsidc.org"""

    assert actual == expected
