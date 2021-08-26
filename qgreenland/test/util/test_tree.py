import anytree
import pytest

from qgreenland.test.constants import TEST_CONFIG_DIR
from qgreenland.util import tree


# def test__manual_ordering_strategy(mock_layer_config_contents):
#     tree._manual_ordering_strategy(mock_layer_config_contents)
# 
#     assert False
# 
# 
# def test__default_ordering_strategy(mock_layer_config_contents_unordered):
#     tree._default_ordering_strategy()
# 
#     assert False
# 
# 
# def test__ordered_directory_contents_manual_strategy(mock_layer_config_contents):
#     tree._ordered_directory_contents()
#     assert False
# 
# 
# def test__ordered_directory_contents_default_strategy(mock_layer_config_contents_unordered):
#     tree._ordered_directory_contents()
#     assert False

def test__tree_from_dir():
    actual_tree = tree._tree_from_dir(TEST_CONFIG_DIR)

    # test that the `Subgroup` is ordered according to `__settings__.py`
    ordered_node = anytree.search.find(
        actual_tree,
        filter_=lambda node: node.name == 'Subgroup',
    )
    expected_manual_ordering = [
        'Foo',
        'example_online',
        'Baz',
        'Bar',
        'example_raster',
    ]
    actual_manual_ordering = [node.name for node in ordered_node.children]
    assert expected_manual_ordering == actual_manual_ordering

    unordered_node = anytree.search.find(
        actual_tree,
        filter_=lambda node: node.name == 'Subgroup without settings',
    )
    expected_default_ordering = [
        'Bar',
        'Baz',
        'Foo',
        'example_online',
        'example_raster',
    ]
    actual_default_ordering = [node.name for node in unordered_node.children]
    assert expected_default_ordering == actual_default_ordering


def test_layer_tree_raises_duplicates_error():
    """The test config dir contains duplicate layers.

    This should raise an error.
    """
    with pytest.raises(RuntimeError):
        tree.layer_tree(TEST_CONFIG_DIR)
