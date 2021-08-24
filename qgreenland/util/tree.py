import pprint
from pathlib import Path
from typing import Optional

import anytree

from qgreenland.constants import CONFIG_DIR


LAYERS_CFG_DIR = CONFIG_DIR / 'layers'


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


def tree_from_dir(
    the_dir: Path,
    parent: Optional[anytree.Node] = None,
) -> anytree.Node:
    """Create a Node tree for given `the_dir`, attached to `parent`."""
    directory_contents = _filter_directory_contents(
        list(the_dir.iterdir()),
    )

    # Check that __order__.py is in the directory! If not, throw an error.
    if not [c for c in directory_contents if c.name == '__order__.py']:
        print(f'__order__.py not found in {the_dir}')

    # Create a node for this directory
    root_node = anytree.Node(the_dir.name, parent=parent)

    # TODO: re-sort `directory_contents` in the order specified by
    # `__order__.py`
    # TODO: remove `__order__.py` from `directory_contents`

    # Loop over things in this directory
    for thing in directory_contents: 
        if thing.is_dir():
            child_node = tree_from_dir(thing, parent=root_node)
        else:
            child_node = anytree.Node(thing.name, parent=root_node)
            
    return root_node


if __name__ == '__main__':
    tree = walk_layers_dir(LAYERS_CFG_DIR)
    for pre, _, node in anytree.RenderTree(tree):
        print(f'{pre}{node.name}')
