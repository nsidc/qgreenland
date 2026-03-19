import csv
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from qgreenland.test.constants import MOCK_COMPILE_PACKAGE_DIR, MOCK_RELEASE_LAYERS_DIR
from qgreenland.util.config import export
from qgreenland.util.config.export import export_config_csv, export_config_manifest


@patch(
    "qgreenland.util.layer.RELEASE_LAYERS_DIR",
    new=MOCK_RELEASE_LAYERS_DIR,
)
def test__layer_manifest_final_assets(full_cfg):
    expected = [
        {
            "checksum": "a9a103f208179726038fa7178747a0a1",
            "file": "example.tif",
            "size_bytes": 287,
            "type": "data",
        },
        {
            "checksum": "22b427acc6e4ebf57052115fdd5ac450",
            "file": "example.tif.aux.xml",
            "size_bytes": 332,
            "type": "ancillary",
        },
    ]

    example_raster_layer_nodes = [
        node for node in full_cfg.layer_tree.leaves if node.name == "example_raster"
    ]
    assert len(example_raster_layer_nodes) == 1
    example_raster_layer_node = example_raster_layer_nodes[0]
    actual = export._layer_manifest_final_assets(example_raster_layer_node)

    assert actual == expected


@patch(
    "qgreenland.util.layer.RELEASE_LAYERS_DIR",
    new=MOCK_RELEASE_LAYERS_DIR,
)
def test_export_config_manifest(full_cfg):
    with tempfile.NamedTemporaryFile("r") as tf:
        export_config_manifest(
            full_cfg,
            output_path=Path(tf.name),
        )

        actual = json.load(tf)

    assert type(actual["qgr_version"]) is str
    assert len(actual["qgr_version"]) >= 6
    del actual["qgr_version"]

    # The config manifest contains only online layers.
    num_offline_layers = len(
        [layer for layer in full_cfg.layers.values() if not layer.is_online_only]
    )
    assert len(actual["layers"]) == num_offline_layers


@patch(
    "qgreenland.util.layer.COMPILE_PACKAGE_DIR",
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test_export_config_csv(full_cfg):
    common = {
        "Data Source Abstract(s)": "Example abstract.;",
        "Data Source Citation(s)": "NSIDC 2020;",
        "Data Source Citation URL(s)": "https://nsidc.org;",
        "Data Source Title(s)": "Example Dataset;",
        "Group": "Group",
        "Layer Description": "Example layer description.",
        "Layer Size": "0 Bytes",
        "Layer Size Bytes": "0",
        "Subgroup": "Subgroup",
    }
    with tempfile.NamedTemporaryFile("r") as tf:
        export_config_csv(
            full_cfg,
            output_path=Path(tf.name),
        )

        actual = list(csv.DictReader(tf))

    expected = [
        {
            **common,
            "Layer Title": "Vector layer used by a VRT",
            "Vector or Raster": "Vector",
            "Layer Size": "106.5 kB",
            "Layer Size Bytes": "106496",
            "Internet Required?": "False",
        },
        {
            **common,
            "Layer Title": "Example online",
            "Vector or Raster": "Raster",
            "Internet Required?": "True",
        },
        {
            **common,
            "Layer Title": "Example raster",
            "Vector or Raster": "Raster",
            "Layer Size": "619 Bytes",
            "Layer Size Bytes": "619",
            "Internet Required?": "False",
        },
        {
            **common,
            "Layer Title": "Vector VRT layer referencing vector_example",
            "Vector or Raster": "Vector",
            "Layer Size": "284 Bytes",
            "Layer Size Bytes": "284",
            "Internet Required?": "False",
            "Subgroup": "Subgroup/Subgroup2",
        },
    ]

    assert actual == expected
