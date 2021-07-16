from typing import List

from qgreenland.config import CONFIG
from qgreenland.runners import RUNNERS



def _fetch_tasks_getter():
    pass


def generate_layer_tasks():
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    tasks = []

    for cfg in CONFIG['layers'].values():
        # TODO: list of what (typing)
        tasks: List = []

        # TODO: Look at `cfg['input']` to figure out which fetch task to use and
        # what params to pass into it.

        task = _fetch_tasks_getter()
        # Look at cfg steps
        for step in cfg['steps']:
            # figure out the correct task and pass kwargs (command, python, template).
            # wait to do templates til the end -- we'll probably need to recurse
            # into the steps within each template. Do we want templates to be
            # nestable? Should templates be able to reference other templates?
            layer_tasks = []
            layer_tasks.append(task)
            for task_type, task_params in step.items():
                task = RUNNERS[task_type](task_params, required_task=task) 
                layer_tasks.append(task)

            # LayerPipeline 
            tasks.append(LayerPipeline(layer_tasks))

        # TODO: figure out what do to about this!!! (add one of these layers as a test)
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        # if cfg['dataset']['access_method'] == 'gdal_remote':
        #     continue

    return tasks
