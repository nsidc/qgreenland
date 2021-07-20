"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import copy
import csv
import functools
import os
from pathlib import Path
from typing import Any, Dict, List, Union

# HACK HACK HACK HACK HACK HACK HACK HACK HACK THIS IS A DUMB HACK HACK HACK
# Importing qgis before fiona is absolutely necessary to avoid segmentation
# faults. They have been occurring in unit tests. We still have no clue why.
import qgis.core as qgc  # noqa: F401
import fiona  # noqa: I100
# HACK HACK HACK HACK HACK HACK HACK HACK HACK THIS IS A DUMB HACK HACK HACK
import yamale
from humanize import naturalsize

import qgreenland.exceptions as exc
from qgreenland.constants import LOCALDATA_DIR
from qgreenland.util.misc import directory_size_bytes, get_layer_path


def _load_config(config_fp: Path, schema_fp: Path) -> Union[Dict, List]:
    """Validate config file against schema with Yamale.

    Yamale can read in directories of config files, so it returns a list of
    (data, fp) tuples. We always read single files, so we return just the data
    from result[0][0].
    """
    schema = yamale.make_schema(schema_fp)
    config = yamale.make_data(config_fp)
    yamale.validate(schema, config, strict=True)

    try:
        return config[0][0]
    except IndexError:
        # TODO: Reconsider this behavior.
        # If there is an empty file, maybe it's intentional. Ignore it.
        return []



def _find_in_list_by_id(haystack: Dict[Any, Any], needle: Any):
    matches = [d for d in haystack if d['id'] == needle]
    if len(matches) > 1:
        raise LookupError(f'Found multiple matches in list with same id: {needle}')

    if len(matches) != 1:
        raise LookupError(f'Found no matches in list with id: {needle}')

    return copy.deepcopy(matches[0])


def _deref_boundaries(cfg: Dict[str, Any]) -> None:
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

        # TODO: remove features and bbox? Just deref to the filepath.
        boundaries_config[boundary_name] = {
            'fp': fp,
            'features': features,
            'bbox': bbox,
        }


def _deref_layers(cfg: Dict[str, Any]) -> None:
    """Dereferences layers in `cfg`, modifying `cfg`.

    Expects boundaries to already be dereferenced.
    """
    layers_config = cfg['layers']
    datasets_config = cfg['datasets']
    project_config = cfg['project']
    for layer_config in layers_config:
        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id = layer_config['input']['dataset']
            asset_id = layer_config['input']['asset']
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['dataset'] = dataset_config

            layer_config['dataset']['asset'] = _find_in_list_by_id(
                dataset_config['assets'],
                asset_id
            )
            del layer_config['dataset']['assets']


def _dereference_config(cfg: Dict[Any, Any]) -> Dict[Any, Any]:
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


def load_configs_from_dir(config_dir: Path, schema_fp: Path) -> List[Any]:
    config: List = []
    for config_fp in Path(config_dir).glob('*.yml'):
        config.extend(_load_config(config_fp, schema_fp))

    return config


@functools.lru_cache(maxsize=None)
def make_config(*, config_dir: Path, schema_dir: Path) -> Dict[str, Any]:
    # TODO: Avoid all this argument drilling without import cycles... this
    # shouldn't be so hard!
    # TODO: Consider namedtuple or something?

    cfg = {
        'project': _load_config(
            config_dir / 'project.yml',
            schema_dir / 'project.yml'
        ),
        'layers': load_configs_from_dir(
            config_dir / 'layers',
            schema_dir / 'layers.yml'
        ),
        # 'layer_groups': _load_config('layer_groups.yml',
        #                              config_dir=config_dir,
        #                              schema_dir=schema_dir),
        'datasets': load_configs_from_dir(
            config_dir / 'datasets',
            schema_dir / 'datasets.yml'
        )
    }

    return _dereference_config(cfg)


def export_config(cfg, output_path='./layers.csv'):
    report = []
    for _, layer in cfg['layers'].items():
        if layer['dataset']['access_method'] != 'gdal_remote':
            layer_dir = Path(get_layer_path(layer)).parent
            layer_size_bytes = directory_size_bytes(layer_dir)
        else:
            # online layers have no size on disk.
            layer_size_bytes = 0

        report.append({
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
            'Layer Size': naturalsize(layer_size_bytes),
            'Layer Size Bytes': layer_size_bytes,
        })

    with open(output_path, 'w') as ofile:
        dict_writer = csv.DictWriter(ofile, report[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f'Exported: {os.path.abspath(ofile.name)}')
