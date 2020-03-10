from functools import partial

from qgreenland.util.misc import get_layer_config


def generate_layer_tasks():
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    layer_cfg = get_layer_config()
    tasks = []

    for cfg in layer_cfg:
        task = cfg['ingest_task']
        kwargs = {'layer_id': cfg['id']}
        kwargs.update(cfg.get('ingest_task_kwargs', {}))

        # TODO: Do we need the partial at all, or can we instantiate the
        # classes here?
        tasks.append(partial(task, **kwargs))

    return tasks
