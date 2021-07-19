from typing import Any, Dict, List, Type

from qgreenland.config import CONFIG
from qgreenland.runners import RUNNERS
from qgreenland.exceptions import QgrRuntimeError
from qgreenland.tasks.common.fetch import FetchTask, FetchDataFiles, FetchCmrGranule
from qgreenland.util.luigi import Finalize


ACCESS_METHODS: Dict[str, Type[FetchTask]] = {
    'http': FetchDataFiles,
    'cmr': FetchCmrGranule,
    'TODO': FetchCmrGranule,
}


def _fetch_task_getter(layer_cfg: Dict[Any, Any]) -> FetchTask:
    dataset_cfg = layer_cfg['dataset']
    asset_cfg = dataset_cfg['asset']
    breakpoint()

    # TODO: come back to access methods, extract constant?
    for access_method in ('http', 'cmr', 'manual'):
        try:
            asset_params = asset_cfg[access_method]
            fetch_task = ACCESS_METHODS[access_method](
                dataset_id=dataset_cfg,
                asset_cfg=asset_cfg,
                **asset_params
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

    for cfg in CONFIG['layers'].values():
        # TODO: list of what (typing)
        tasks: List[LayerTask] = []

        # TODO: Look at `cfg['input']` to figure out which fetch task to use and
        # what params to pass into it.
        task = _fetch_task_getter(cfg)

        breakpoint()

        for step in cfg['steps']:
            # figure out the correct task and pass kwargs (command, python, template).
            # wait to do templates til the end -- we'll probably need to recurse
            # into the steps within each template. Do we want templates to be
            # nestable? Should templates be able to reference other templates?
            for task_type, task_params in step.items():
                task = RUNNERS[task_type](task_params, required_task=task, layer_id=layer_id) 

            # We only need the last task in the layer pipeline to run all
            # previous tasks.
            layer_final_task = Finalize(requires_task=task)
            tasks.append(layer_final_task)

        # TODO: figure out what do to about this!!! (add one of these layers as a test)
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        # if cfg['dataset']['access_method'] == 'gdal_remote':
        #     continue

    return tasks
