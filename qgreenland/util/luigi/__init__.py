from collections.abc import Generator
from functools import cache

from qgreenland.models.config.asset import (
    AnyAsset,
    CmrAsset,
    CommandAsset,
    HttpAsset,
    ManualAsset,
    OnlineAsset,
    RepositoryAsset,
)
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer
from qgreenland.util.config.config import get_config
from qgreenland.util.luigi.tasks.fetch import (
    FetchCmrGranule,
    FetchDataFiles,
    FetchDataWithCommand,
    FetchLocalDataFiles,
    FetchTask,
    MergeFetchedDataTask,
)
from qgreenland.util.luigi.tasks.main import ChainableTask, FinalizeTask

# TODO: Make "fetch" tasks into Python "steps"?
ASSET_TYPE_TASKS: dict[type[AnyAsset], type[FetchTask]] = {
    CmrAsset: FetchCmrGranule,
    CommandAsset: FetchDataWithCommand,
    HttpAsset: FetchDataFiles,
    # TODO: rename `FetchLocalDataFiles`, split in two!
    ManualAsset: FetchLocalDataFiles,
    RepositoryAsset: FetchLocalDataFiles,
}


def _fetch_task(
    dataset_cfg: Dataset,
    asset_cfg: AnyAsset,
) -> FetchTask:
    # TODO: Unit test!
    fetch_task = ASSET_TYPE_TASKS[type(asset_cfg)](
        dataset_id=dataset_cfg.id,
        asset_id=asset_cfg.id,
    )

    return fetch_task


def fetch_tasks_from_layer(
    layer_cfg: Layer,
) -> list[FetchTask]:
    # TODO: Unit test!
    tasks = []
    for dataset_input in layer_cfg.inputs:
        # Check if it's an online layer; those have no fetching or processing
        # pipeline.
        if isinstance(dataset_input.asset, OnlineAsset):
            continue

        dataset_cfg = dataset_input.dataset
        asset_cfg = dataset_input.asset
        tasks.append(_fetch_task(dataset_cfg, asset_cfg))

    return tasks


def fetch_tasks_from_dataset(
    dataset_cfg: Dataset,
) -> Generator[FetchTask, None, None]:
    # TODO: Unit test!
    for asset_cfg in dataset_cfg.assets.values():
        yield _fetch_task(dataset_cfg, asset_cfg)


@cache
def generate_fetch_only_pipelines() -> list[FetchTask]:
    """Generate a list of fetch-only tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    config = get_config()
    tasks: list[FetchTask] = []

    layers = config.layers.values()

    for layer_cfg in layers:
        # Create tasks, making each task dependent on the previous task.
        tasks = fetch_tasks_from_layer(layer_cfg)
        tasks.extend(tasks)

    return tasks


@cache
def generate_layer_pipelines() -> list[FinalizeTask]:
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    config = get_config()
    tasks: list[FinalizeTask] = []

    layers = config.layers.values()

    for layer_cfg in layers:
        step_number = -1

        if layer_cfg.is_online_only:
            continue

        # Create tasks, making each task dependent on the previous task.
        task: list[MergeFetchedDataTask] | ChainableTask
        task = MergeFetchedDataTask(
            requires_fetch_tasks=fetch_tasks_from_layer(layer_cfg)
        )

        # If the layer has no steps, it's just fetched and finalized.
        if layer_cfg.steps:
            for _step in layer_cfg.steps:
                step_number += 1
                task = ChainableTask(
                    requires_task=task,
                    layer_id=layer_cfg.id,
                    step_number=step_number,
                )

        # We only need the last task in the layer pipeline to run all
        # "required" tasks in a layer pipeline.
        final_task = FinalizeTask(
            requires_task=task,
            layer_id=layer_cfg.id,
        )

        tasks.append(final_task)

    return tasks
