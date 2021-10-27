from functools import cache
from pathlib import Path

import qgreenland.exceptions as exc
from qgreenland.config.project import project
from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.util.module import load_objects_from_paths_by_class
from qgreenland.util.tree import LayerNode, layer_tree


def _get_python_module_filepaths(the_dir: Path) -> list[Path]:
    """Return non-dunder python modules found in `the_dir`."""
    if not the_dir.is_dir():
        raise RuntimeError(
            f'Given path {the_dir} is not a directory.',
        )

    return [
        f
        for f in list(the_dir.glob('**/*.py'))
        if not (f.stem.startswith('__') and f.stem.endswith('__'))
    ]


def compile_datasets_cfg(config_dir: Path) -> dict[str, ConfigDataset]:
    """Find and return all datasets in "`config_dir`/datasets"."""
    datasets_dir = config_dir / 'datasets'
    dataset_fps = _get_python_module_filepaths(datasets_dir)
    datasets = load_objects_from_paths_by_class(
        dataset_fps,
        target_class=ConfigDataset,
    )

    return {dataset.id: dataset for dataset in datasets}


@cache
def compile_cfg(
    config_dir: Path,
    *,
    include_patterns: tuple[str, ...] = (),
    exclude_patterns: tuple[str, ...] = (),
    exclude_manual_assets: bool = False,
) -> Config:
    try:
        compiled_layer_tree = layer_tree(
            config_dir / 'layers',
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            exclude_manual_assets=exclude_manual_assets,
        )
        leaves = compiled_layer_tree.leaves

        if not all(type(leaf) is LayerNode for leaf in leaves):
            raise RuntimeError('Error compiling config. Please debug.')

        layers_dict = {
            node.layer_cfg.id: node.layer_cfg
            for node in leaves
        }

        return Config(
            project=project,
            layers=layers_dict,
            datasets=compile_datasets_cfg(config_dir),
            layer_tree=compiled_layer_tree,
        )
    except Exception as e:
        raise exc.QgrConfigCompileError(f'Failed to compile config. {e}')
