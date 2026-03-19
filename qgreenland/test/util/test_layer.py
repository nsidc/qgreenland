from pathlib import Path

import qgreenland.util.layer as layer_util


def test_get_layer_path_by_id(full_cfg, vector_vrt_layer_cfg):
    layer_path = layer_util.get_layer_path_by_id(vector_vrt_layer_cfg.id)

    assert layer_path == f"Group/Subgroup/Subgroup2/{vector_vrt_layer_cfg.title}"


def test_get_vrt_ref_data_relpath(full_cfg, vector_layer_cfg, vector_vrt_layer_cfg):
    actual = layer_util.get_vrt_ref_data_relpath(vector_vrt_layer_cfg)

    related_layer_id = vector_vrt_layer_cfg.inputs[0].layer_id
    expected = Path(f"../../{vector_layer_cfg.title}/{related_layer_id}.gpkg")

    assert actual == expected
