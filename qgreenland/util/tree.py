import copy
import json
import logging
from abc import ABC
from fnmatch import fnmatch
from functools import cached_property
from pathlib import Path
from typing import Any, Optional, Union

import anytree
import funcy
from anytree.exporter import DictExporter

import qgreenland.exceptions as exc
from qgreenland.constants.paths import LAYERS_CFG_DIR
from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.layer import Layer
from qgreenland.models.config.layer_group import (
    AnyGroupSettings,
    LayerGroupSettings,
    RootGroupSettings,
)
from qgreenland.util.json import MagicJSONEncoder
from qgreenland.util.misc import find_duplicates
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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name="{self.name}")'

    def __json__(self) -> dict[Any, Any]:
        """Help JSONEncoder serialize the tree."""
        exporter = DictExporter()
        return exporter.export(self)


class LayerNode(QgrTreeNode):
    """A Node with a reference to a layer configuration."""

    layer_cfg: Layer

    def __init__(self, *args, layer_cfg: Layer, **kwargs):
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
    exclude_manual_assets: bool = False,
) -> anytree.Node:
    tree = _tree_from_dir(
        layer_cfg_dir,
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
        exclude_manual_assets=exclude_manual_assets,
    )

    # Clean up any empty layer groups. This shouldn't happen normally, but if
    # any layers are included or excluded, it's likely.
    tree = prune_empty_groups(tree)

    if len(tree.children) == 0:
        raise exc.QgrNoLayersFoundError(
            f'No layers found matching {include_patterns=}; {exclude_patterns=}',
        )

    duplicates = find_duplicates(node.name for node in tree.leaves)
    if duplicates:
        raise exc.QgrInvalidConfigError(
            f'Duplicate layer_ids found: {duplicates}',
        )

    return tree


def leaf_lookup(
    tree: anytree.Node,
    target_node_name: str,
) -> LayerNode:
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
            and not p.name.startswith('.')
        )

    return [
        p for p in paths
        if _path_valid(p)
    ]


LayerDirectoryElement = Union[Path, Layer]


def _explode_config_layers_from_python_files(
    paths: list[Path],
) -> list[LayerDirectoryElement]:
    """Explode Layers from Python files, with directory paths intact.

    Any paths which are not Python files or directories will trigger an
    exception.
    """
    result: list[LayerDirectoryElement] = []

    for path in paths:
        if path.suffix == '.py':
            config_layers = load_objects_from_paths_by_class(
                [path],
                target_class=Layer,
            )
            result.extend(config_layers)
        else:
            if not path.is_dir():
                raise RuntimeError(
                    f'Paths in {path.parent} must be Python files or'
                    f' directories. Found: {path}',
                )
            result.append(path)

    return result


def _default_ordering_strategy(
    layers_and_groups: list[LayerDirectoryElement],
) -> list[LayerDirectoryElement]:
    """Sort configuration elements within `layers_and_groups`.

    Directories first, sorted alphabetically. Then Layers, sorted
    alphabetically by title.
    """
    ordered_directory_elements: list[LayerDirectoryElement] = []

    directories = [e for e in layers_and_groups if isinstance(e, Path)]
    directories.sort(key=lambda path: path.name)
    ordered_directory_elements.extend(directories)

    layer_cfgs = [e for e in layers_and_groups if type(e) is Layer]
    layer_cfgs.sort(key=lambda layer_cfg: layer_cfg.title)
    ordered_directory_elements.extend(layer_cfgs)

    return ordered_directory_elements


def _manual_ordering_strategy(
    layers_and_groups: list[LayerDirectoryElement],
    settings: AnyGroupSettings,
) -> list[LayerDirectoryElement]:
    """Sort `layers_and_groups` using `settings.order` as a guide."""
    ordered_directory_elements: list[LayerDirectoryElement] = []

    if not settings.order:
        raise RuntimeError('Order must be specified in settings.')

    for s in settings.order:
        try:
            if s.startswith(':'):
                matcher = lambda x: isinstance(x, Layer) and x.id == s[1:]
                thing_desc = f'layer id "{s[1:]}"'
            else:
                matcher = lambda x: isinstance(x, Path) and x.name == s
                thing_desc = f'group/directory "{s}"'

            matches = funcy.lfilter(matcher, layers_and_groups)
            if len(matches) != 1:
                raise RuntimeError(
                    f'Expected to find {thing_desc}. Found: {matches}',
                )

            thing = matches[0]
        except Exception as e:
            raise RuntimeError(
                f'Unexpected error processing `settings.order` element "{s}".'
                f' {e}',
            )

        ordered_directory_elements.append(thing)

    return ordered_directory_elements


def _validate_ordered(
    *,
    unordered_layers_and_groups: list[LayerDirectoryElement],
    ordered_layers_and_groups: list[LayerDirectoryElement],
) -> None:
    """Validate that `ordered_directory_elements` is comprehensive.

    All `LayerDirectoryElement`s found in `unordered_layers_and_groups` must be
    present in `ordered_layers_and_groups`. Return any elements which are not.
    """
    ondisk_set = {
        json.dumps(e, cls=MagicJSONEncoder, sort_keys=True)
        for e in unordered_layers_and_groups
    }
    ordered_set = {
        json.dumps(e, cls=MagicJSONEncoder, sort_keys=True)
        for e in ordered_layers_and_groups
    }

    if (diff := ondisk_set - ordered_set) != set():
        raise RuntimeError(
            f'Found the following items on disk but not in ordered set: {diff}',
        )
    if (diff := ordered_set - ondisk_set) != set():
        raise RuntimeError(
            f'Found the following items in ordered set but not on disk: {diff}',
        )


def _ordered_layers_and_groups(
    the_dir: Path,
    *,
    is_root: bool,
) -> tuple[list[LayerDirectoryElement], AnyGroupSettings]:
    """Examine `the_dir` for layers and groups and sort them.

    Layers are represented as `Layer` objects in Python files. Each Python
    file is converted to its internal `Layer` objects.

    Groups are represented as directories and are returned unchanged.
    """
    (
        layer_and_group_paths,
        settings,
        settings_path,
    ) = _handle_layer_config_directory(
        the_dir,
        is_root=is_root,
    )

    layers_and_groups = _explode_config_layers_from_python_files(
        layer_and_group_paths,
    )

    try:
        if settings.order:
            error_hint = '. Check `__settings__.py`'
            ordered = _manual_ordering_strategy(layers_and_groups, settings)
        else:
            error_hint = ''
            ordered = _default_ordering_strategy(layers_and_groups)

        _validate_ordered(
            unordered_layers_and_groups=layers_and_groups,
            ordered_layers_and_groups=ordered,
        )
    except Exception as e:
        raise RuntimeError(
            f'Error ordering layers in `{the_dir}`{error_hint}. {e}',
        )

    return ordered, settings


def _handle_layer_config_directory(
    the_dir: Path,
    *,
    is_root: bool,
) -> tuple[list[Path], AnyGroupSettings, Optional[Path]]:
    """Load settings and contents from given directory path."""
    directory_contents = _filter_directory_contents(
        list(the_dir.iterdir()),
    )
    settings_fps = [
        c for c in directory_contents
        if c.name == '__settings__.py'
    ]

    if not settings_fps:
        logger.debug(f'__settings__.py not found in {the_dir}')
        if is_root:
            settings = RootGroupSettings()
        else:
            settings = LayerGroupSettings()

        return (directory_contents, settings, None)

    if len(settings_fps) != 1:
        raise RuntimeError(
            f'Expected exactly one settings file. Received: {settings_fps}',
        )
    settings_fp = settings_fps[0]

    settings_objects = load_objects_from_paths_by_class(
        [settings_fp],
        target_class=RootGroupSettings,
    )

    if len(settings_objects) != 1:
        raise RuntimeError(
            f'Expected exactly one settings object in {settings_fp}',
        )
    settings = settings_objects[0]

    layer_and_group_paths = [
        c for c in directory_contents
        if c.name != '__settings__.py'
    ]

    return (layer_and_group_paths, settings, settings_fp)


def _matches_filters(
    candidate: Layer,
    *,
    include_patterns: tuple[str, ...],
    exclude_patterns: tuple[str, ...],
    exclude_manual_assets: bool = False,
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
    if (
        exclude_manual_assets
        and type(candidate.input.asset) is ManualAsset
    ):
        # TODO: `included = True` instead? This would be more consistent with
        # the "included or not excluded" behavior the patterns follow.
        return False

    if not (include_patterns or exclude_patterns):
        return True

    # Does candidate match any of the include_patterns? If there are no
    # patterns, it's included.
    included = any(fnmatch(candidate.id, p) for p in include_patterns)
    if not exclude_patterns:
        return included

    # Does candidate match any of the exclude_patterns?
    excluded = any(fnmatch(candidate.id, p) for p in exclude_patterns)
    if not include_patterns:
        return not excluded

    # Include things which are both excluded and included.
    result = not excluded or included
    # Alternative strategy:
    # result = included and not excluded

    return result


def _tree_from_dir(
    the_dir: Path,
    parent: Optional[anytree.Node] = None,
    include_patterns: tuple[str, ...] = (),
    exclude_patterns: tuple[str, ...] = (),
    exclude_manual_assets: bool = False,
) -> anytree.Node:
    """Create a Node tree for given `the_dir`, attached to `parent`."""
    ordered_layers_and_groups, settings = _ordered_layers_and_groups(
        the_dir,
        is_root=(not bool(parent)),
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
                exclude_manual_assets=exclude_manual_assets,
            )
        elif isinstance(thing, Layer):
            if _matches_filters(
                thing,
                include_patterns=include_patterns,
                exclude_patterns=exclude_patterns,
                exclude_manual_assets=exclude_manual_assets,
            ):
                # NOTE: Since this modifies the entire tree (`root_node`),
                # nothing needs to be assigned here.
                LayerNode(thing.id, layer_cfg=thing, parent=root_node)
            else:
                logger.debug(
                    f'Layer {thing.id} does not match patterns:'
                    f' {include_patterns=}; {exclude_patterns=};'
                    f' {exclude_manual_assets=}',
                )

        else:
            raise RuntimeError(
                f'Found unexpected thing: {thing}',
            )

    return root_node


def _delete_node(
    node: anytree.node,
    msg: str = 'Removing node',
) -> None:
    """Delete (_"delete"_) the node by orphaning it and letting the GC kill it.

    Yes, this is the right way :)
        https://github.com/c0fec0de/anytree/issues/152
    """
    node_path = list(node.group_name_path) + [node.name]
    node_name = '/'.join(node_path)
    logger.warn(f'{msg}: /{node_name}')
    node.parent = None


def prune_layers_not_in_package(
    tree: LayerGroupNode,
) -> LayerGroupNode:
    """Remove any leaf nodes that are `not in_package`.

    If there are any empty groups after this, remove them too.
    """
    lt = copy.deepcopy(tree)

    # We can iterate using tree.leaves here because we know all LayerNodes are
    # leaves. Removing these leaves shouldn't create new LayerNode leaves.
    for node in lt.leaves:
        if type(node) is LayerNode and not node.layer_cfg.in_package:
            _delete_node(node, msg='Removing layer not in package')

    lt = prune_empty_groups(lt)
    return lt


def prune_empty_groups(
    tree: LayerGroupNode,
) -> LayerGroupNode:
    """Remove any leaf nodes which are not LayerNodes."""
    lt = copy.deepcopy(tree)

    # NOTE: We MUST iterate using PostOrderIter(lt) instead of lt.leaves
    # because removing a leaf group may leave its parent group newly enleafened.
    for node in anytree.PostOrderIter(lt):
        if node.is_leaf and type(node) is not LayerNode:
            logger.warn(f'{node.group_name_path=}, {node.name=}')
            _delete_node(node, msg='Removing empty group')

    return lt


if __name__ == '__main__':
    tree = layer_tree(LAYERS_CFG_DIR)
    print(tree.render())
