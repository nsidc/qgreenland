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


def _make_step_tasks(
    steps_cfg: List[Dict[Any, Any]],
    requires_task: ChainableTask,
    layer_id: str,
) -> List[ChainableTask]:
    """From a list of steps, create tasks.

    For "template" steps, which are really collections of steps, recurse.
    """
    # TODO: Should we return a list or just the final task?
    tasks = []

    for step_number, step in enumerate(steps_cfg):

        # TODO: Is this readable?
        if tasks:
            requires_task = tasks[-1]

        # TODO: Handle templates...
        if step['type'] == 'template':
            template_steps_cfg = load_yaml_template(
                step['template']['name'],
                kwargs=step['template']['kwargs']
            )

            tasks.extend(
                # Recurse!
                _make_step_tasks(
                    steps_cfg=template_steps_cfg,
                    requires_task=tasks[-1],
                    layer_id=layer_id,
                )
            )

        else:
            task = ChainableTask(
                requires_task=requires_task,
                layer_id=layer_id,
                step_number=step_number,
            )
        tasks.append(task)

    return tasks


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
        first_task = _fetch_task_getter(layer_cfg)

        step_tasks = _make_step_tasks(
            steps_cfg=layer_cfg['steps'],
            requires_task=first_task,
            layer_id=layer_id,
        )

        # We only need the last task in the layer pipeline to run all
        # previous tasks.
        # TODO: Is `final_task` a good name? What about just `task`?
        final_task = FinalizeTask(
            requires_task=step_tasks[-1],
            layer_id=layer_id,
        )
        tasks.append(final_task)

        # TODO: figure out what do to about this!!! (add one of these layers as a test)
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        # if layer_cfg['dataset']['access_method'] == 'gdal_remote':
        #     continue

    return tasks
