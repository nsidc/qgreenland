import anytree
import pytest

from qgreenland.test.constants import TEST_CONFIG_DIR
from qgreenland.models.config.layer_group import RootGroupSettings
from qgreenland.util import tree


def test__tree_from_dir():
    """
    TODO: more assertions.

    - assert that all branch nodes are LayerGroupNode
    - assert that all leaf nodes are LayerNode

    - assert that non-root branch nodes as a LayerGroupSettings
    """
    actual_tree = tree._tree_from_dir(TEST_CONFIG_DIR)

    # The root of the tree should contain a `RootGroupSettings`
    assert isinstance(actual_tree.settings, RootGroupSettings)

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

    # Assert that all leaf nodes are instances of `LayerNode`.
    assert all([isinstance(node, tree.LayerNode) for node in actual_tree.leaves])


def test_layer_tree_raises_duplicates_error():
    """The test config dir contains duplicate layers.

    This should raise an error.
    """
    with pytest.raises(RuntimeError):
        tree.layer_tree(TEST_CONFIG_DIR)
