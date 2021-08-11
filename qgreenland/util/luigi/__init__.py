from typing import Dict, List, Type

import luigi

from qgreenland.config import CONFIG
from qgreenland.models.config.dataset import (
    AnyAsset,
    ConfigDatasetCmrAsset,
    ConfigDatasetHttpAsset,
)
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.luigi.tasks.fetch import FetchCmrGranule, FetchDataFiles, FetchTask
from qgreenland.util.luigi.tasks.main import ChainableTask, FinalizeTask


# TODO: Make "fetch" tasks into Python "steps".
ASSET_TYPE_TASKS: Dict[Type[AnyAsset], Type[FetchTask]] = {
    ConfigDatasetHttpAsset: FetchDataFiles,
    ConfigDatasetCmrAsset: FetchCmrGranule,
}


# TODO: Unit test!
def _fetch_task_getter(layer_cfg: ConfigLayer) -> FetchTask:
    dataset_cfg = layer_cfg.input.dataset
    asset_cfg = layer_cfg.input.asset

    fetch_task = ASSET_TYPE_TASKS[type(asset_cfg)](
        dataset_id=dataset_cfg.id,
        asset_id=asset_cfg.id,
    )

    return fetch_task


# Generate layer pipelines?
def generate_layer_tasks():
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    tasks: List[luigi.Task] = []

    for layer_cfg in CONFIG.layers.values():
        # Check if it's an online layer; those have no processing pipeline.
        if layer_cfg.input.type == 'online':
            continue

        # Create tasks, making each task dependent on the previous task.
        task = _fetch_task_getter(layer_cfg)

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
