from qgreenland.constants import CONFIG
from qgreenland.tasks.layers import INGEST_TASKS


def generate_layer_tasks():
    """Generate a list of pre-configured tasks based on layer configuration.

    Instead of calling tasks now, we return a list of callables with the
    arguments already populated.
    """
    tasks = []

    for cfg in CONFIG['layers'].values():
        # `gdal_remote` layers are accessed by QGIS from a remote location, so
        # no processing is required.
        if cfg['dataset']['access_method'] == 'gdal_remote':
            continue

        task = INGEST_TASKS[cfg['ingest_task']]
        tasks.append(task(layer_id=cfg['id']))

    return tasks
