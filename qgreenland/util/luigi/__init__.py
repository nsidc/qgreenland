from functools import cache
from typing import Generator, Type

import luigi
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
)
from qgreenland.util.luigi.tasks.main import ChainableTask, FinalizeTask

# TODO: Make "fetch" tasks into Python "steps"?
ASSET_TYPE_TASKS: dict[Type[AnyAsset], Type[FetchTask]] = {
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


def fetch_task_from_layer(
    layer_cfg: Layer,
) -> FetchTask:
    # TODO: Unit test!
    dataset_cfg = layer_cfg.input.dataset
    asset_cfg = layer_cfg.input.asset

    return _fetch_task(dataset_cfg, asset_cfg)


def fetch_tasks_from_dataset(
    dataset_cfg: Dataset,
) -> Generator[FetchTask, None, None]:
    # TODO: Unit test!
    for asset_cfg in dataset_cfg.assets.values():
        yield _fetch_task(dataset_cfg, asset_cfg)


@cache
def generate_layer_pipelines(
    *,
    fetch_only: bool = False,
) -> list[luigi.Task]:
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    config = get_config()
    tasks: list[luigi.Task] = []

    layers = config.layers.values()

    for layer_cfg in layers:
        # Check if it's an online layer; those have no fetching or processing
        # pipeline.
        if isinstance(layer_cfg.input.asset, OnlineAsset):
            continue

        # Create tasks, making each task dependent on the previous task.
        task = fetch_task_from_layer(layer_cfg)
        if fetch_only:
            tasks.append(task)
            continue

        # If the layer has no steps, it's just fetched and finalized.
        if layer_cfg.steps:
            for step_number, _ in enumerate(layer_cfg.steps):
                task = ChainableTask(
                    requires_task=task,
                    layer_id=layer_cfg.id,
                    step_number=step_number,
                )

        # We only need the last task in the layer pipeline to run all
        # "required" tasks in a layer pipeline.
        task = FinalizeTask(
            requires_task=task,
            layer_id=layer_cfg.id,
        )

        tasks.append(task)

    return tasks
