import importlib
import inspect
from pathlib import Path
from types import ModuleType
from typing import Type, TypeVar

from qgreenland.config.project import project
from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer


ModelClass = TypeVar('ModelClass')


def _find_models_in_module(
    module: ModuleType,
    model_class: Type[ModelClass],
) -> list[ModelClass]:
    """Find all objects of class `model_class` among `module` members."""
    module_members = inspect.getmembers(module)
    return [
        m[1] for m in module_members
        if isinstance(m[1], model_class)
    ]


def _load_models_from_modules(
    module_paths: list[Path],
    *,
    model_class: Type[ModelClass],
) -> list[ModelClass]:
    """Return all objects of class `model_class` in `module_paths`."""
    found_models = []
    for module_path in module_paths:
        module_spec = importlib.util.spec_from_file_location(
            # TODO: Maybe `split` on `os.path.sep`?
            f'_generated_module.{module_path.stem}',
            str(module_path),
        )
        if not module_spec:
            raise RuntimeError(f'No module found at {module_path}')

        module = importlib.util.module_from_spec(module_spec)

        # https://github.com/python/typeshed/issues/2793
        if not isinstance(module_spec.loader, importlib.abc.Loader):
            raise RuntimeError(
                f'Module {module_path} failed to load:'
                ' (module_spec.loader=None)',
            )
        # TODO: Put a syntax error or runtime error (1/0) in the module. What
        # happens? Unit test this with a tempfile?
        module_spec.loader.exec_module(module)

        # TODO: Validate `id`s of each model, if present, are unique? Do that
        # afterwards? Probably after.

        models = _find_models_in_module(module, model_class=model_class)
        found_models.extend(models)

    return found_models


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
    datasets = _load_models_from_modules(
        dataset_fps,
        model_class=ConfigDataset,
    )

    return {dataset.id: dataset for dataset in datasets}


def compile_layers_cfg(config_dir: Path) -> dict[str, ConfigLayer]:
    """Find and return all datasets in "`config_dir`/layers"."""
    # TODO: DRY this and the above function?
    layers_dir = config_dir / 'layers'
    layer_fps = _get_python_module_fps(layers_dir)
    layers = _load_models_from_modules(
        layer_fps,
        model_class=ConfigLayer,
    )

    return {layer.id: layer for layer in layers}


# TODO: Accept a Path and look for expected structure at that path, then
# dynamically load things.
def compile_cfg(config_dir: Path) -> Config:
    return Config(
        project=project,
        layers=compile_layers_cfg(config_dir),
        datasets=compile_datasets_cfg(config_dir),
        # TODO: ...
        hierarchy_settings=[],
    )


THIS_DIR = Path(__file__).resolve().parent
CONFIG = compile_cfg(THIS_DIR)
