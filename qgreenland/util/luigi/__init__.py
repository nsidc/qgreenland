from typing import Dict, List, Type

import luigi

from qgreenland.config import CONFIG
from qgreenland.exceptions import QgrRuntimeError
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.luigi.tasks.fetch import FetchCmrGranule, FetchDataFiles, FetchTask
from qgreenland.util.luigi.tasks.main import ChainableTask, FinalizeTask


# TODO: Make "fetch" tasks into Python "steps".
ACCESS_METHODS: Dict[str, Type[FetchTask]] = {
    'http': FetchDataFiles,
    'cmr': FetchCmrGranule,
    'TODO': FetchCmrGranule,
}


def _fetch_task_getter(layer_cfg: ConfigLayer) -> FetchTask:
    dataset_cfg = layer_cfg.input.dataset
    asset_cfg = layer_cfg.input.asset

    # TODO: come back to access methods, extract constant?
    if asset_cfg.type not in ('http', 'cmr', 'manual'):
        raise QgrRuntimeError('Found asset config without expected access method.')

    fetch_task = ACCESS_METHODS[asset_cfg.type](
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
    tasks = []

    for layer_cfg in CONFIG.layers.values():
        layer_id = layer_cfg.id
        tasks: List[luigi.Task] = []

        # Create tasks, making each task dependent on the previous task.
        task = _fetch_task_getter(layer_cfg)

        for step_number, _ in enumerate(layer_cfg.steps):
            task = ChainableTask(
                requires_task=task,
                layer_id=layer_id,
                step_number=step_number,
            )

        # We only need the last task in the layer pipeline to run all
        # "required" tasks in a layer pipeline.
        task = FinalizeTask(
            requires_task=task,
            layer_id=layer_id,
        )
        tasks.append(task)

        # TODO: figure out what do to about this!!! (add one of these layers as a test)
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        # if layer_cfg['dataset']['access_method'] == 'gdal_remote':
        #     continue

    return tasks
