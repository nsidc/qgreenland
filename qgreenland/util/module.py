import importlib
import inspect
from pathlib import Path
from types import ModuleType
from typing import Type, TypeVar


def module_from_path(module_path: Path) -> ModuleType:
    module_spec = importlib.util.spec_from_file_location(
        # TODO: Maybe `split` on `os.path.sep`?
        f"_generated_module.{module_path.stem}",
        str(module_path),
    )
    if not module_path.is_file() or not module_spec:
        raise FileNotFoundError(f"No module found at {module_path}")

    module = importlib.util.module_from_spec(module_spec)

    # https://github.com/python/typeshed/issues/2793
    if not isinstance(module_spec.loader, importlib.abc.Loader):
        raise RuntimeError(
            f"Module {module_path} failed to load:" " (module_spec.loader=None)",
        )

    module_spec.loader.exec_module(module)
    return module


T = TypeVar("T")


# TODO: Operate on a single path
def load_objects_from_paths_by_class(
    module_paths: list[Path],
    *,
    target_class: Type[T],
) -> list[T]:
    """Return all objects of class `model_class` in `module_paths`."""
    found_models = []
    for module_path in module_paths:
        module = module_from_path(module_path)

        # TODO: Validate `id`s of each model, if present, are unique? Do that
        # afterwards? At the very end, examine each leaf?

        models = _find_in_module_by_class(module, target_class=target_class)
        found_models.extend(models)

    return found_models


def _find_in_module_by_class(
    module: ModuleType,
    target_class: Type[T],
) -> list[T]:
    """Find all objects of class `model_class` among `module` members."""
    module_members = inspect.getmembers(module)
    matches = [m[1] for m in module_members if isinstance(m[1], target_class)]

    # Also look one level deep in iterables, facilitating list comprehensions in
    # config
    iterables = [
        m[1]
        for m in module_members
        if isinstance(m[1], tuple) or isinstance(m[1], list)
    ]
    matches_in_iterables = [
        m for iterable in iterables for m in iterable if isinstance(m, target_class)
    ]

    matches.extend(matches_in_iterables)
    return matches
