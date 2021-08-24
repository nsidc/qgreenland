from pathlib import Path

from qgreenland.config.project import project
from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.tree import tree_from_dir
from qgreenland.util.module import load_objects_from_paths_by_class


THIS_DIR = Path(__file__).resolve().parent


def _get_python_module_fps(the_dir: Path) -> list[Path]:
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
    dataset_fps = _get_python_module_fps(datasets_dir)
    datasets = load_objects_from_paths_by_class(
        dataset_fps,
        target_class=ConfigDataset,
    )

    return {dataset.id: dataset for dataset in datasets}


def compile_layers_cfg(config_dir: Path) -> dict[str, ConfigLayer]:
    """Find and return all datasets in "`config_dir`/layers"."""
    # TODO: DRY this and the above function?
    layers_dir = config_dir / 'layers'
    layer_fps = _get_python_module_fps(layers_dir)
    layers = load_objects_from_paths_by_class(
        layer_fps,
        target_class=ConfigLayer,
    )

    return {layer.id: layer for layer in layers}


# TODO: Accept a Path and look for expected structure at that path, then
# dynamically load things.
def compile_cfg(config_dir: Path) -> Config:
    return Config(
        project=project,
        layers=compile_layers_cfg(config_dir),
        datasets=compile_datasets_cfg(config_dir),
        layer_tree=tree_from_dir(THIS_DIR / 'layers'),
    )


CONFIG = compile_cfg(THIS_DIR)
