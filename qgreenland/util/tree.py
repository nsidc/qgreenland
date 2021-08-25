import logging
import pprint
import re
from functools import cached_property
from pathlib import Path
from typing import Dict, Optional, Union

import anytree

from qgreenland.constants import CONFIG_DIR
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.layer_group import (
    AnyGroupSettings,
    LayerGroupSettings,
    RootGroupSettings,
)
from qgreenland.util.module import (
    load_objects_from_paths_by_class,
    module_from_path,
)


LAYERS_CFG_DIR = CONFIG_DIR / 'layers'
logger = logging.getLogger('luigi-interface')


class LayerNode(anytree.Node):
    """A Node with a reference to a layer configuration."""
    layer_cfg: ConfigLayer

    def __init__(self, *args, layer_cfg: ConfigLayer, **kwargs):
        self.layer_cfg = layer_cfg
        super().__init__(*args, **kwargs)

    # TODO: DRY. Mixin?
    @cached_property
    def group_node_path(self):
        return _node_group_path(self)

    @cached_property
    def group_name_path(self):
        return _node_group_name_path(self)


class LayerGroupNode(anytree.Node):
    """A Node with layer group settings."""
    settings: AnyGroupSettings

    def __init__(self, *args, settings: AnyGroupSettings, **kwargs):
        self.settings = settings
        super().__init__(*args, **kwargs)

    # TODO: DRY. Mixin?
    @cached_property
    def group_node_path(self):
        return _node_group_path(self)

    @cached_property
    def group_name_path(self):
        return _node_group_name_path(self)


AnyNode = Union[LayerGroupNode, LayerNode]

# TODO: rename to 'parent_group_name_path' and 'parent_group_node_path'

def _node_group_path(node: AnyNode) -> tuple[AnyNode]:
    """Produce a list of group/directory nodes a layer/group node lives in.

    Omit the root node (named "layers" after the "layers" directory) and omit
    the given node, leaving only parent group nodes.
    """
    return node.path[1:-1]


def _node_group_name_path(node: AnyNode) -> tuple[str]:
    """Produce a list of group/directory names a layer/group node lives in."""
    return tuple(group_node.name for group_node in _node_group_path(node))


def render_tree(tree: anytree.Node) -> str:
    result = ''
    for pre, _, node in anytree.RenderTree(tree):
        result += f'{pre}{node.name}\n'

    return result.removesuffix('\n')


def _filter_directory_contents(paths=list[Path]) -> list[Path]:
    """Returns the contents of the directory we care about."""
    def _path_valid(p: Path) -> bool:
        return (
            (p.is_dir or p.suffix == '.py')
            and not p.name == '__pycache__'
        )

    return [
        p for p in paths
        if _path_valid(p)
    ]

"""
* Input: `some_dir`, `parent_node: Optional[anytree.Node]`
* Look at the things inside it
    * Throw an error if __order__.py is not inside

=== IMPLEMENTED ABOVE THIS LINE ===

* somedir_ordered: list[Union[Path, ConfigLayer]]
* If `__order__.py` is not present, use a default ordering strategy to create
  `some_dir_ordered`.
  * Groups first, alphabetically
  * Layers last, alphabetically by `layer.title`
  * Emit a debug log statement "__order__.py not found in `some_dir`, using
    default ordering."
* If `__order__.py` is present, validate and dereference to create
  `somedir_ordered`. Compare __order__.py contents to the directory contents to
  ensure everything in `some_dir` is enumerated.
    * Assert set(directory contents).pop(__order__.py) == set(__order__ file|dir references)
    * Assert set(module references) == set(modules in `some_dir`)
    * Assert set(module:ConfigLayer references) == set(ConfigLayers in modules)
    * Assert set(ConfigLayers in modules) == list(ConfigLayers in modules) (no
      dupes)?
    * Store dereferenced ConfigLayers.
* Iterate over `some_dir_ordered` to build a `anytree.Node` (`for element in
  some_dir_ordered:`)
    * Is `element` a directory?
        * Recurse into the directory (start at the top with the new directory as
        `some_dir`)! This returns a Node with the current node as a parent.
    * Is element a `ConfigLayer`?
        * Create a Node(ConfigLayer.id, parent=parent_node)


=== OBE NOTES BELOW THIS LINE ===
* Dereference `__order__.py` ? why not just use `imports` in these files?
  :shrug:
    * Ensure all `ConfigLayer`s defined in `some_dir` are enumerated in
      `__order__.py`. I don't think Vulture can do this.
    * Throw in error if layer not present in `__order__.py`
    * Throw an error if reference to non-existent layer is present in
      `__order__.py` (We get this out-of-the box if we switch from references
      and dynamic imports to static imports)
    * Get the `id` from each `ConfigLayer` reference
    * Create a Node from the layer id.
"""
LayerDirectoryElement = Union[Path, ConfigLayer]


def _dereference_order_element(
    element: str,
    parent_dir: Path,
) -> LayerDirectoryElement:
    """Convert `element` to the thing it's referencing.

    `element` can reference an object in a Python file, e.g.
    `file.py:<object_name>`, or it can reference a directory.
    """
    pattern = re.compile(r'^(?P<filename>\w+\.py):(?P<layer_id>\w+)$')
    if match := pattern.match(element):
        filename = match.group('filename')
        layer_id = match.group('layer_id')

        layers = load_objects_from_paths_by_class(
            [parent_dir / filename],
            target_class=ConfigLayer
        )
        result = [l for l in layers if l.id == layer_id][0]
    else:
        result = parent_dir / element

    return result


def _default_ordering_strategy(
    paths: list[Path],
) -> list[LayerDirectoryElement]:
    """Sort `paths` alphabetically, directories first.

    ConfigLayers are sorted by title.
    """
    # TODO: Everything!
    return paths


def _manual_ordering_strategy(
    paths: list[Path],
    order_strings: list[str],
) -> list[LayerDirectoryElement]:
    """Sort with `order_strings` as a guide.

    Validate that all ConfigLayers and directories in `paths` are enumerated
    exactly once in `order_strings`.
    """
    # All paths are siblings, so it doesn't matter which we use to get parent:
    parent_dir = paths[0].parent

    dereferenced_order = [
        _dereference_order_element(e, parent_dir=parent_dir)
        for e in order_strings
    ]

    # TODO: Validate... validate what?
    return dereferenced_order
    


def _ordered_directory_contents(
    directory_contents: list[Path],
    settings: AnyGroupSettings,
) -> list[LayerDirectoryElement]:
    if settings.order:
        return _manual_ordering_strategy(directory_contents, settings.order)
    else:
        return _default_ordering_strategy(directory_contents)


def _handle_layer_config_directory(
    the_dir: Path,
) -> tuple[list[Path], AnyGroupSettings]:
    """Load settings and contents from given directory path."""
    directory_contents = _filter_directory_contents(
        list(the_dir.iterdir()),
    )
    settings_fp = [
        c for c in directory_contents
        if c.name == '__settings__.py'
    ]

    if not settings_fp:
        # How do we know if this is a "root" group?
        logger.debug(f'__settings__.py not found in {the_dir}')
        return (directory_contents, LayerGroupSettings())

    settings_fp = settings_fp[0]
    settings_objects = load_objects_from_paths_by_class(
        [settings_fp],
        target_class=RootGroupSettings,
    )
    if len(settings_objects) != 1:
        raise RuntimeError(
            f'Expected exactly one settings object in{settings_fp}',
        )

    cleansed_directory_contents = [
        c for c in directory_contents
        if c.name != '__settings__.py'
    ]
    settings = settings_objects[0]

    return (cleansed_directory_contents, settings)


def _tree_from_dir(
    the_dir: Path,
    parent: Optional[anytree.Node] = None,
) -> anytree.Node:
    """Create a Node tree for given `the_dir`, attached to `parent`."""
    directory_contents, settings = _handle_layer_config_directory(the_dir)

    ordered_directory_contents = _ordered_directory_contents(
        directory_contents,
        settings=settings,
    )

    # Create a node for this directory
    root_node = LayerGroupNode(the_dir.name, settings=settings, parent=parent)

    # Loop over things in this directory
    for thing in ordered_directory_contents: 
        if isinstance(thing, Path):
            if not thing.is_dir():
                raise RuntimeError(f'Expected {thing} to be a directory!')

            child_node = _tree_from_dir(thing, parent=root_node)
        elif isinstance(thing, ConfigLayer):
            child_node = LayerNode(
                thing.id,
                layer_cfg=thing,
                parent=root_node,
            )
        else:
            raise RuntimeError(
                'Found unexpected thing: {thing}'
            )
            
    return root_node


def layer_tree() -> anytree.Node:
    # TODO: Look up a layer for each leaf
    tree = _tree_from_dir(LAYERS_CFG_DIR)
    _check_for_duplicate_leaves(tree)

    return tree


def _check_for_duplicate_leaves(tree: anytree.Node) -> None:
    if len(set(tree.leaves)) != len(tree.leaves):
        # TODO: Print duplicates
        raise RuntimeError(f'Duplicate leaves found in tree: {tree.leaves}')


# TODO: Re-order functions
def leaf_lookup(
    tree: anytree.Node,
    target_node_name: str,
) -> LayerNode:
    _check_for_duplicate_leaves(tree)

    matches = [l for l in tree.leaves if l.name == target_node_name]
    if len(matches) != 1:
        raise RuntimeError(
            f'Found not-one matches: {matches}'
        )

    return matches[0]



if __name__ == '__main__':
    tree = layer_tree()
    print(render_tree(tree))
