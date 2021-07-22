from typing import Any, Dict, List, Type

from qgreenland.config import CONFIG
from qgreenland.runners import RUNNERS
from qgreenland.exceptions import QgrRuntimeError
from qgreenland.util.luigi.tasks.fetch import FetchTask, FetchDataFiles, FetchCmrGranule
from qgreenland.util.luigi.tasks.main import ChainableTask, FinalizeTask


# TODO: Make "fetch" tasks into Python "steps".
ACCESS_METHODS: Dict[str, Type[FetchTask]] = {
    'http': FetchDataFiles,
    'cmr': FetchCmrGranule,
    'TODO': FetchCmrGranule,
}


def _fetch_task_getter(layer_cfg: Dict[Any, Any]) -> FetchTask:
    dataset_cfg = layer_cfg['dataset']
    asset_cfg = dataset_cfg['asset']

    # TODO: come back to access methods, extract constant?
    for access_method in ('http', 'cmr', 'manual'):
        try:
            # Test that we're looking at the right asset
            asset_cfg[access_method]

            fetch_task = ACCESS_METHODS[access_method](
                dataset_cfg=dataset_cfg,
                asset_cfg=asset_cfg,
            )
            return fetch_task
        except KeyError:
            pass

    raise QgrRuntimeError('Found asset config without expected access method.')


def generate_layer_tasks():
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    tasks = []

    for layer_cfg in CONFIG['layers'].values():
        layer_id = layer_cfg['id']
        tasks: List[LayerTask] = []

        # Create tasks, making each task dependent on the previous task.
        task = _fetch_task_getter(layer_cfg)
        for step_number, step in enumerate(layer_cfg['steps']):
            task = ChainableTask(
                requires_task=task,
                layer_id=layer_id,
                step_number=step_number,
            )

        # We only need the last task in the layer pipeline to run all
        # previous tasks.
        # TODO: Is `layer_final_task` a good name? What about just `task`?
        layer_final_task = FinalizeTask(
            requires_task=task,
            layer_id=layer_id,
        )
        tasks.append(layer_final_task)

        # TODO: figure out what do to about this!!! (add one of these layers as a test)
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        # if layer_cfg['dataset']['access_method'] == 'gdal_remote':
        #     continue

    return tasks
