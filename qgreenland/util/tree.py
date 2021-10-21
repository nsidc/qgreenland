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
    *,
    include_patterns: tuple[str, ...] = (),
    exclude_patterns: tuple[str, ...] = (),
) -> anytree.Node:
    tree = _tree_from_dir(
        layer_cfg_dir,
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
    )
    # Clean up any empty layer groups. This shouldn't happen normally, but if
    # any layers are included or excluded, it's likely.
    _prune_tree(tree)

    if len(tree.children) == 0:
        raise exc.QgrNoLayersFoundError(
            f'No layers found matching {include_patterns=}; {exclude_patterns=}',
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
            (p.suffix == '.py' or p.is_dir)
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


def _explode_config_layers_from_python_files(
    paths: list[Path],
) -> list[LayerDirectoryElement]:
    """Explode ConfigLayers from Python files, with directory paths intact.

    Any paths which are not Python files or directories will trigger an
    exception.
    """
    result: list[LayerDirectoryElement] = []

    for path in paths:
        if path.suffix == '.py':
            config_layers = load_objects_from_paths_by_class(
                [path],
                ConfigLayer,
            )
            result.extend(config_layers)
        else:
            if not path.is_dir():
                raise RuntimeError(
                    f'Paths in {path.parent} must be Python files or'
                    ' directories. Found: {path}',
                )
            result.append(path)

    return result


def _default_ordering_strategy(
    layers_and_groups: list[LayerDirectoryElement],
) -> list[LayerDirectoryElement]:
    """Sort configuration elements within `layers_and_groups`.

    Directories first, sorted alphabetically. Then ConfigLayers, sorted
    alphabetically by title.
    """
    ordered_directory_elements: list[LayerDirectoryElement] = []

    # Get the directories first and sort alphabetically.
    directories = (e for e in layers_and_groups if type(e) is Path)
    directories.sort(key=lambda path: path.name)
    breakpoint()
    ordered_directory_elements.extend(directories)

    layer_cfgs = (e for e in layers_and_groups if type(e) is ConfigLayer)
    layer_cfgs.sort(key=lambda layer_cfg: layer_cfg.title)
    breakpoint()
    ordered_directory_elements.extend(layer_cfgs)

    if set(ordered_directory_elements) != set(layers_and_groups):
        raise RuntimeError(
            f'Expected directory contents {layers_and_groups=} to contain the'
            f'same items after sorting {ordered_directory_elements=}'
        )

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


def _ordered_layers_and_groups(
    directory_contents: list[Path],
    settings: AnyGroupSettings,
) -> list[LayerDirectoryElement]:
    """Examine `directory_contents` for layers and groups and sort them.

    Layers are represented as `ConfigLayer` objects in Python files. Each Python
    file is converted to its internal `ConfigLayer` objects.

    Groups are represented as directories and are returned unchanged.
    """
    layers_and_groups = _explode_config_layers_from_python_files(
        directory_contents,
    )

    if settings.order:
        return _manual_ordering_strategy(layers_and_groups, settings.order)
    else:
        return _default_ordering_strategy(layers_and_groups)


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

    layer_and_group_paths = [
        c for c in directory_contents
        if c.name != '__settings__.py'
    ]
    settings = settings_objects[0]

    return (layer_and_group_paths, settings)


def _matches_filters(
    candidate: str,
    *,
    include_patterns: tuple[str, ...],
    exclude_patterns: tuple[str, ...],
) -> bool:
    """Determine if candidate matches given filters.

    Since we don't allow the user to specify the order inclusion and exclusion
    is performed in, we chose to prioritize inclusions. e.g.:

        include: bed*
        exclude: bedmachine_thickness

    Do we include or exclude bedmachine_thickness? It matches both the general
    include and specific exclude. With prioritizing inclusions, this filter will
    have no effect because the result is (all layers - bedmachine_thickness) +
    all bedmachine layers.

    and:

        include: bedmachine_error
        exclude: bed*

    Do we include or exclude bedmachine_error? It matches both the specific
    include and the general exclude. With prioritizing inclusions, the result is
    the (all layers - all bedmachine layers) + bedmachine_error.

    In both cases, we get different results depending on whether we prioritize
    inclusions or exclusions. I.e.: for set of inclusions I and exclusions E,
    this is a question of `I - E` vs. `!E + I`.
    """
    if not (include_patterns or exclude_patterns):
        return True

    # Does candidate match any of the include_patterns? If there are no
    # patterns, it's included.
    included = any(fnmatch(candidate, p) for p in include_patterns)
    if not exclude_patterns:
        return included

    # Does candidate match any of the exclude_patterns?
    excluded = any(fnmatch(candidate, p) for p in exclude_patterns)
    if not include_patterns:
        return not excluded

    # Include things which are both excluded and included.
    result = not excluded or included
    # Alternative strategy:
    # result = included and not excluded

    return result


def _validate_ordered_layers_and_groups(
    ordered_layers_and_groups: list[LayerDirectoryElement],
    directory_contents: list[Path],
) -> list[LayerDirectoryElement]:
    """Validate that `ordered_layers_and_groups` is comprehensive.

    All `LayerDirectoryElement`s found in `directory_contents` must be present
    in `ordered_layers_and_groups`. Return any elements which are not.
    """






def _tree_from_dir(
    the_dir: Path,
    parent: Optional[anytree.Node] = None,
    include_patterns: tuple[str, ...] = (),
    exclude_patterns: tuple[str, ...] = (),
) -> anytree.Node:
    """Create a Node tree for given `the_dir`, attached to `parent`."""
    layer_and_group_paths, settings = _handle_layer_config_directory(
        the_dir,
        is_root=(not bool(parent)),
    )

    ordered_layers_and_groups = _ordered_layers_and_groups(
        layer_and_group_paths,
        settings=settings,
    )
    # list[Union[Path, ConfigLayer]]

    # Validate that `ordered_layers_and_groups` contains all `ConfigLayer`
    # objects and directory paths present in `the_dir`.
    deselected_layers = _validate_ordered_layers_and_groups(
        ordered_layers_and_groups,
        directory_contents=layer_and_group_paths,

    )
    if ...:
        raise RuntimeError(
            'The following objects were present in {the_dir} but could not be'
            ' sorted: {...}. Does your `__settings__.py` enumerate all layers'
            ' and directories?',
        )

    # Create a node for this directory
    root_node = LayerGroupNode(the_dir.name, settings=settings, parent=parent)

    # Loop over things in this directory
    for thing in ordered_layers_and_groups:
        if isinstance(thing, Path):
            if not thing.is_dir():
                raise RuntimeError(f'Expected {thing} to be a directory!')

            # NOTE: Since this modifies the entire tree (`root_node`), nothing
            # needs to be assigned here.
            _tree_from_dir(
                thing,
                parent=root_node,
                include_patterns=include_patterns,
                exclude_patterns=exclude_patterns,
            )
        elif isinstance(thing, ConfigLayer):
            # NOTE: Since this modifies the entire tree (`root_node`), nothing
            # needs to be assigned here.
            if _matches_filters(
                thing.id,
                include_patterns=include_patterns,
                exclude_patterns=exclude_patterns,
            ):
                LayerNode(thing.id, layer_cfg=thing, parent=root_node)
            else:
                logger.debug(
                    f'Layer {thing.id} does not match patterns:'
                    f' {include_patterns=}; {exclude_patterns=}',
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
