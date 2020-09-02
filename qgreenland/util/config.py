"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import copy
import csv
import os

import yamale


def _load_config(config_filename, *, config_dir, schema_dir):
    """Validate config file against schema with Yamale.

    It is expected that the given config filename in CONFIG_DIR has a schema of
    matching name in CONFIG_SCHEMA_DIR.

    Yamale can read in directories of config files, so it returns a list of
    (data, fp) tuples. We always read single files, so we return just the data
    from result[0][0].
    """
    config_fp = os.path.join(config_dir, config_filename)
    schema_fp = os.path.join(schema_dir, config_filename)

    if not os.path.isfile(config_fp):
        raise NotImplementedError(
            'Loading is supported for only one config file at a time.'
        )

    schema = yamale.make_schema(schema_fp)
    config = yamale.make_data(config_fp)
    yamale.validate(schema, config, strict=True)

    return config[0][0]


def _dereference_config(cfg):
    """Take a full configuration object, replace references with the referent.

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

    layers_config = cfg['layers']
    datasets_config = cfg['datasets']

    for layer_config in layers_config:
        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id, source_id = layer_config['data_source'].split('.')
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['dataset'] = dataset_config

            layer_config['source'] = _find_in_list_by_id(dataset_config['sources'],
                                                         source_id)
            del layer_config['dataset']['sources']

        # TODO: Populate related layer group configuration? Instead of
        # accessing CONFIG['layers'][layer_id], allow direct access by
        # CONFIG[layer_id]

        # TODO: Populate layer_config['extent'] with referenced value in project
        # config.
        # breakpoint()

    # Turn layers config in to a dict keyed by id
    cfg['layers'] = {x['id']: x for x in cfg['layers']}

    return cfg


def make_config(*, config_dir, schema_dir):
    # TODO: Avoid all this argument drilling without import cycles... this
    # shouldn't be so hard!
    # TODO: Consider namedtuple or something?
    cfg = {
        'project': _load_config('project.yml',
                                config_dir=config_dir,
                                schema_dir=schema_dir),
        'layers': _load_config('layers.yml',
                               config_dir=config_dir,
                               schema_dir=schema_dir),
        'layer_groups': _load_config('layer_groups.yml',
                                     config_dir=config_dir,
                                     schema_dir=schema_dir),
        'datasets': _load_config('datasets.yml',
                                 config_dir=config_dir,
                                 schema_dir=schema_dir)
    }

    return _dereference_config(cfg)


def export_config(cfg, output_path='./layers.csv'):
    report = [{
        'Group': layer['group_path'].split('/', 1)[0],
        'Subgroup': (layer['group_path'].split('/', 1)[1]
                     if '/' in layer['group_path'] else ''),
        'Layer Title': layer['title'],
        'Layer Description': layer.get('description', ''),
        'Vector or Raster': layer['data_type'],
        'Data Source Title': layer['dataset']['metadata']['title'],
        'Data Source Abstract': layer['dataset']['metadata']['abstract'],
        'Data Source Citation': layer['dataset']['metadata']['citation']['text'],
        'Data Source Citation URL': layer['dataset']['metadata']['citation']['url'],
    } for _, layer in cfg['layers'].items()]

    with open(output_path, 'w') as ofile:
        dict_writer = csv.DictWriter(ofile, report[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f'Exported: {os.path.abspath(ofile.name)}')
