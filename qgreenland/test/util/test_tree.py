import anytree
import pytest

from qgreenland.test.constants import TEST_CONFIG_DIR
from qgreenland.models.config.layer_group import LayerGroupSettings, RootGroupSettings
from qgreenland.util import tree


def test__tree_from_dir():
    """Test tree._tree_from_dir"""
    actual_tree = tree._tree_from_dir(TEST_CONFIG_DIR)

    # The root of the tree should contain a `RootGroupSettings`
    assert isinstance(actual_tree.settings, RootGroupSettings)

    branches = anytree.search.findall(actual_tree, filter_=lambda node: not node.is_leaf)
    # Assert that all branches are instances of LayerGroupNode.
    assert all(
        isinstance(branch, tree.LayerGroupNode)
        for branch in branches
    )

    # Assert that all non-root branches have `settings` of instance `LayerGroupSettings`
    branches_excluding_root = branches[1:]
    assert all(
        isinstance(branch.settings, LayerGroupSettings)
        for branch in branches_excluding_root
    )

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
    assert all(
        isinstance(node, tree.LayerNode)
        for node in actual_tree.leaves
    )


def test_layer_tree_raises_duplicates_error():
    """The test config dir contains duplicate layers.

    This should raise an error.
    """
    with pytest.raises(RuntimeError):
        tree.layer_tree(TEST_CONFIG_DIR)
