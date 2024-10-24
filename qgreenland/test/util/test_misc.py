from qgreenland.constants.paths import COMPILE_PACKAGE_DIR
from qgreenland.util import layer as layer_util


def test_layer_compile_dir(raster_layer_node):
    expected = COMPILE_PACKAGE_DIR / "foo" / "Group" / "Subgroup" / "Example raster"
    actual = layer_util.get_layer_compile_dir(raster_layer_node, package_name="foo")

    assert expected == actual


def test_vector_or_raster(online_layer_node):
    assert layer_util.vector_or_raster(online_layer_node) == "Raster"
