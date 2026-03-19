import qgreenland.util.layer as layer_util


def test_get_layer_path_by_id(full_cfg, vector_vrt_layer_cfg):
    layer_path = layer_util.get_layer_path_by_id("example_vector_vrt")

    assert layer_path == f"Group/Subgroup/Subgroup2/{vector_vrt_layer_cfg.title}"
