import os

import yamale

from qgreenland.constants import PACKAGE_DIR

CONFIG_DIR = f'{PACKAGE_DIR}/config'
CONFIG_SCHEMA_DIR = f'{CONFIG_DIR}/schema'


def _load_config(config_filename):
    """Validate config file against schema with Yamale.

    It is expected that the given config filename in CONFIG_DIR has a schema of
    matching name in CONFIG_SCHEMA_DIR.

    Yamale can read in directories of config files, so it returns a list of
    (data, fp) tuples. We always read single files, so we return just the data
    from result[0][0].
    """
    config_fp = os.path.join(CONFIG_DIR, config_filename)
    schema_fp = os.path.join(CONFIG_SCHEMA_DIR, config_filename)

    if not os.path.isfile(config_fp):
        return NotImplementedError(
            'Loading is supported for only one config file at a time.'
        )

    schema = yamale.make_schema(schema_fp)
    config = yamale.make_data(config_fp)
    yamale.validate(schema, config, strict=True)

    return config[0][0]


def dereference_config(cfg):
    """Takes a full configuration object, replaces references with the referent.

    - Datasets
    - Sources
    - Ingest Tasks
    """
    def _find_in_list_by_id(haystack, needle):
        matches = [d for d in haystack if d['id'] == needle]
        if len(matches) > 1:
            raise LookupError(f'Found multiple matches in list with same id: {needle}')

        if len(matches) != 1:
            raise LookupError(f'Found no matches in list with id: {needle}')

        return copy.deepcopy(matches[0])

    # This import is in a function body because circular import.
    # TODO: Straighten out this spaghetti
    from qgreenland.tasks.layers import INGEST_TASKS

    layers_config = cfg['layers']
    datasets_config = cfg['datasets']

    for layer_config in layers_config:
        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id, source_id = layer_config['data_source'].split('.')
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['dataset'] = dataset_config

            layer_config['source'] = _find_in_list_by_id(dataset_config['sources'], source_id)
            del layer_config['dataset']['sources']

        # Populate ingest_task with the real function
        if type(layer_config['ingest_task']) is str:
            layer_config['ingest_task'] = INGEST_TASKS[layer_config['ingest_task']]

    return layers_config


def get_layer_config(layer_id=None):
    """Get the full layer config or a single layer's config after dereferencing."""
    layers_config = dereference_config()

    if not layer_id:
        return layers_config

    try:
        return _find_in_list_by_id(layers_config, layer_id)
    except LookupError:
        raise NotImplementedError(
            f"Configuration for layer '{layer_id}' not found."
        )


CONFIG = {
    'layers': _load_config('layers.yml'),
    'layer_groups': _load_config('layer_groups.yml'),
    'datasets': _load_config('datasets.yml')
}

CONFIG = dereference_config(CONFIG)
