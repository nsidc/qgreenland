"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import copy
import csv
import functools
import os
from pathlib import Path

# HACK HACK HACK HACK HACK HACK HACK HACK HACK THIS IS A DUMB HACK HACK HACK
# Importing qgis before fiona is absolutely necessary to avoid segmentation
# faults. They have been occurring in unit tests. We still have no clue why.
import qgis.core as qgc  # noqa: F401
import fiona  # noqa: I100
# HACK HACK HACK HACK HACK HACK HACK HACK HACK THIS IS A DUMB HACK HACK HACK
import yamale
from humanize import naturalsize  # type: ignore

import qgreenland.exceptions as exc
from qgreenland.constants import LOCALDATA_DIR
from qgreenland.util.misc import get_layer_path


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


def _find_in_list_by_id(haystack, needle):
    matches = [d for d in haystack if d['id'] == needle]
    if len(matches) > 1:
        raise LookupError(f'Found multiple matches in list with same id: {needle}')

    if len(matches) != 1:
        raise LookupError(f'Found no matches in list with id: {needle}')

    return copy.deepcopy(matches[0])


def _deref_boundaries(cfg):
    """Dereference project boundaries, modifying `cfg`.

    Replace project boundary value (filename) with an object containing
    useful information about the boundary file.
    """
    boundaries_config = cfg['project']['boundaries']
    for boundary_name, boundary_fn in boundaries_config.items():
        fp = os.path.join(LOCALDATA_DIR, boundary_fn)
        with fiona.open(fp) as ifile:
            features = list(ifile)
            meta = ifile.meta
            bbox = ifile.bounds

        if (feature_count := len(features)) != 1:
            raise exc.QgrInvalidConfigError(
                f'Configured boundary {boundary_name} contains the wrong'
                f' number of features. Expected 1, got {feature_count}.'
            )

        if (boundary_crs := meta['crs']['init'].lower()) \
           != (project_crs := cfg['project']['crs'].lower()):
            raise exc.QgrInvalidConfigError(
                f'Expected CRS of boundary file {fp} ({boundary_crs}) to'
                f' match project CRS ({project_crs}).'
            )

        boundaries_config[boundary_name] = {
            'fp': fp,
            'features': features,
            'bbox': bbox,
        }


def _deref_layers(cfg):
    """Dereferences layers in `cfg`, modifying `cfg`.

    Expects boundaries to already be dereferenced.
    """
    layers_config = cfg['layers']
    datasets_config = cfg['datasets']
    project_config = cfg['project']
    for layer_config in layers_config:
        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id, source_id = layer_config['data_source'].split('.')
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['dataset'] = dataset_config

            layer_config['source'] = _find_in_list_by_id(dataset_config['sources'],
                                                         source_id)
            del layer_config['dataset']['sources']

        # Always default to the background extent
        boundary_name = layer_config.get('boundary', 'background')

        layer_config['boundary'] = project_config['boundaries'][boundary_name]


def _dereference_config(cfg):
    """Take a full configuration object, replace references with the referent.

    - Datasets
    - Sources
    - Ingest Tasks
    """
    _deref_boundaries(cfg)
    _deref_layers(cfg)

    # Turn layers config in to a dict keyed by id TODO: we should ensure that
    # all objects in the CONFIG are immutable. We need to do a deepcopy here
    # because the use of YAML anchors(`&`)/references(`*`) in the config yml
    # files result in config objects that are copied by reference, not by
    # value. So, if we try to e.g., `pop` an element from a list in the config,
    # it will affect all other pieces of config that reference that data.
    cfg['layers'] = {x['id']: copy.deepcopy(x) for x in cfg['layers']}

    return cfg


@functools.lru_cache(maxsize=None)
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
        'Layer Size': (naturalsize(Path(get_layer_path(layer)).stat().st_size)
                       if layer['dataset']['access_method'] != 'gdal_remote' else ''),
    } for _, layer in cfg['layers'].items()]

    with open(output_path, 'w') as ofile:
        dict_writer = csv.DictWriter(ofile, report[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f'Exported: {os.path.abspath(ofile.name)}')
