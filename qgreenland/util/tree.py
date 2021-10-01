import logging
import re
from abc import ABC
from fnmatch import fnmatch
from functools import cached_property
from pathlib import Path
from typing import Any, Optional, Union

import anytree
from anytree.exporter import DictExporter

import qgreenland.exceptions as exc
from qgreenland.constants import LAYERS_CFG_DIR
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.layer_group import (
    AnyGroupSettings,
    LayerGroupSettings,
    RootGroupSettings,
)
from qgreenland.util.module import (
    load_objects_from_paths_by_class,
)


logger = logging.getLogger('luigi-interface')


class QgrTreeNode(anytree.Node, ABC):
    """Provide helpers for accessing the layer tree group path.

    The Anytree documentation suggests using mixins, but this looks like it
    works too and is maybe more straightforward.
    """

    @cached_property
    def group_node_path(self) -> tuple['QgrTreeNode']:
        """Produce a list of group/directory nodes a layer/group node lives in.

        Omit the root node (named "layers" after the "layers" directory) and omit
        the given node, leaving only parent group nodes.
        """
        return self.path[1:-1]

    @cached_property
    def group_name_path(self) -> tuple[str, ...]:
        """Produce a list of group/directory names a layer/group node lives in."""
        return tuple(
            str(group_node.name)
            for group_node in self.group_node_path
        )

    def render(self) -> str:
        result = ''
        for pre, _, node in anytree.RenderTree(self):
            result += f'{pre}{node.name}\n'

        return result.removesuffix('\n')

    def __json__(self) -> dict[Any, Any]:
        """Help JSONEncoder serialize the tree."""
        exporter = DictExporter()
        return exporter.export(self)


class LayerNode(QgrTreeNode):
    """A Node with a reference to a layer configuration."""

    layer_cfg: ConfigLayer

    def __init__(self, *args, layer_cfg: ConfigLayer, **kwargs):
        self.layer_cfg = layer_cfg
        super().__init__(*args, **kwargs)


class LayerGroupNode(QgrTreeNode):
    """A Node with layer group settings."""

    settings: AnyGroupSettings

    def __init__(self, *args, settings: AnyGroupSettings, **kwargs):
        self.settings = settings
        super().__init__(*args, **kwargs)


def layer_tree(
    layer_cfg_dir: Path,
    pattern: Optional[str],
) -> anytree.Node:
    tree = _tree_from_dir(layer_cfg_dir, pattern=pattern)
    _prune_tree(tree)

    if len(tree.children) == 0:
        raise exc.QgrNoLayersFoundError(
            f'No layers found matching {pattern=}',
        )

    _check_for_duplicate_leaves(tree)

    return tree


def leaf_lookup(
    tree: anytree.Node,
    target_node_name: str,
) -> LayerNode:
    _check_for_duplicate_leaves(tree)

    matches = [
        leaf for leaf in tree.leaves
        if leaf.name == target_node_name
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f'Found not-one matches: {matches}',
        )

    return matches[0]


def _filter_directory_contents(paths=list[Path]) -> list[Path]:
    """Return the `paths` to include only those we care about."""
    def _path_valid(p: Path) -> bool:
        return (
            (p.is_dir or p.suffix == '.py')
            and not p.name == '__pycache__'
        )

    return [
        p for p in paths
        if _path_valid(p)
    ]


# TODO: Validate order against directory contents
#   * Assert set(directory contents).pop(__settings__.py) == set(__order__
#     file|dir references)
#   * Assert set(module references) == set(modules in `some_dir`)
#   * Assert set(module:ConfigLayer references) == set(ConfigLayers in modules)
#   * Assert set(ConfigLayers in modules) == list(ConfigLayers in modules) (no
#     Dupes)?

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
            target_class=ConfigLayer,
        )
        if not layers:
            raise RuntimeError(
                f'No match found for {element} in {parent_dir}.',
            )

        try:
            return [
                layer for layer in layers
                if layer.id == layer_id
            ][0]
        except IndexError:
            found_layers = [layer.id for layer in layers]
            raise RuntimeError(
                f'Failed to find layer with id {layer_id}.'
                f' Found layers with ids: {found_layers}.',
            )
    else:
        return parent_dir / element


def _default_ordering_strategy(
    paths: list[Path],
) -> list[LayerDirectoryElement]:
    """Sort configuration elements within `paths`.

    A configuration element can be a directory (one of the `paths`), or a
    ConfigLayer Python object contained by a Python file. A Python file (one of
    the `paths`) can contain multiple ConfigLayer objects.

    Directories first, sorted alphabetically. Then ConfigLayers, sorted
    alphabetically by title.
    """
    ordered_directory_elements: list[LayerDirectoryElement] = []

    # Get the directories first and sort alphabetically.
    sorted_directories = sorted(
        (path for path in paths if path.is_dir()),
        key=lambda path: path.name,
    )
    ordered_directory_elements.extend(sorted_directories)

    # Find any python files in `paths`
    python_files = [path for path in paths if path.is_file() and path.suffix == '.py']
    # Read all of the ConfigLayer objects out of them python files
    layer_cfgs = load_objects_from_paths_by_class(
        python_files,
        target_class=ConfigLayer,
    )

    # Sort the ConfigLayer objects by title.
    layer_cfgs.sort(key=lambda layer_cfg: layer_cfg.title)

    # Extend `ordered_directory_elements` with ordered ConfigLayer objects.
    ordered_directory_elements.extend(layer_cfgs)

    return ordered_directory_elements


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

    # TODO: Validate...
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
    *,
    is_root: bool,
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
        logger.debug(f'__settings__.py not found in {the_dir}')
        if is_root:
            settings = RootGroupSettings()
        else:
            settings = LayerGroupSettings()

        return (directory_contents, settings)

    settings_objects = load_objects_from_paths_by_class(
        settings_fp,
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
    pattern: Optional[str] = None,
) -> anytree.Node:
    """Create a Node tree for given `the_dir`, attached to `parent`."""
    directory_contents, settings = _handle_layer_config_directory(
        the_dir,
        is_root=(not bool(parent)),
    )

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

            # NOTE: Since this modifies the entire tree (`root_node`), nothing
            # needs to be assigned here.
            _tree_from_dir(thing, parent=root_node, pattern=pattern)
        elif isinstance(thing, ConfigLayer):
            # NOTE: Since this modifies the entire tree (`root_node`), nothing
            # needs to be assigned here.
            if pattern and fnmatch(thing.id, pattern):
                LayerNode(
                    thing.id,
                    layer_cfg=thing,
                    parent=root_node,
                )
            else:
                logger.debug(
                    f'Layer {thing.id} does not match pattern "{pattern}"',
                )

        else:
            raise RuntimeError(
                f'Found unexpected thing: {thing}',
            )

    return root_node


def _check_for_duplicate_leaves(tree: anytree.Node) -> None:
    all_layer_ids = [node.name for node in tree.leaves]
    if len(set(all_layer_ids)) != len(all_layer_ids):
        # TODO: Print duplicates
        raise RuntimeError(f'Duplicate leaves found in tree: {tree.leaves}')


def _prune_tree(tree: anytree.Node) -> None:
    """Remove any leaf nodes which are not LayerNodes."""
    for node in anytree.PostOrderIter(tree):
        if node.is_leaf and type(node) is not LayerNode:
            # "Delete" the node by orphaning it and letting the garbage
            # collector kill it. Yes, this is the right way :)
            #    https://github.com/c0fec0de/anytree/issues/152
            node_path = list(node.group_name_path) + [node.name]
            node_name = '/'.join(node_path)
            logger.debug(f'Removing leaf group: /{node_name}')
            node.parent = None


if __name__ == '__main__':
    tree = layer_tree(LAYERS_CFG_DIR)
    print(tree.render())
