"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import copy
import csv
import functools
import itertools
import logging
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple, TypeVar, Union

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
from qgreenland.models.config import Config
from qgreenland.util.misc import (
    directory_size_bytes,
    get_final_layer_filepath,
    vector_or_raster,
)


logger = logging.getLogger('luigi-interface')
DEFAULT_LAYER_MANIFEST_PATH = Path('./layers.csv')


def _load_config(*, config_fp: Path, schema_fp: Path) -> Union[Dict, List]:
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
            'bbox': {
                'min_x': bbox[0],
                'min_y': bbox[1],
                'max_x': bbox[2],
                'max_y': bbox[3],
            },
        }


class PartialFormatDict(dict):
    """Hack to enable partial formatting of strings with {slugs}.

    e.g.:

        '{foo} {bar}, {baz}'.format_map(
            PartialFormatDict(foo='Hello', bar='there')
        )
        >>> 'Hello there, {baz}'
    """

    def __missing__(self, key):
        return '{' + key + '}'


DictOrList = TypeVar(
    'DictOrList',
    Dict[Any, Any],
    Tuple[Any],
    List[Any],
)


def _interpolate_nested_values(
    thing: DictOrList,
    **kwargs,
) -> DictOrList:
    """Interpolate all strings found in `thing` with `kwargs`.

    WARNING: Mutates `thing`!
    """
    items: Iterable[Any]
    if isinstance(thing, dict):
        items = thing.items()
    elif isinstance(thing, list):
        items = enumerate(thing)
    elif isinstance(thing, str):
        return thing.format_map(PartialFormatDict(**kwargs))
    else:
        return thing

    for key, value in items:
        # 🌶️ Recurse 🌶️!
        thing[key] = _interpolate_nested_values(value, **kwargs)

    return thing


def _interpolate_template_kwargs(
    template: Dict[str, Any],
    **kwargs: Dict[str, Any],
) -> List[Dict[str, Any]]:
    # TODO: kwarg default values (i.e. optional kwargs) would be cool to
    # provide. Careful, cowboy, we're getting into Jinja-like templating
    # territory.

    # Validate all kwargs are passed
    if set(template['kwargs']) != set(kwargs.keys()):
        raise exc.QgrInvalidConfigError(
            f"Expected kwargs: {template['kwargs']}.\n"
            f'Received kwargs: {kwargs}'
        )

    return _interpolate_nested_values(
        template['steps'],
        **kwargs,
    )


def _deref_steps(
    steps: List[Dict[str, Any]],
    *,
    templates: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """Dereference layer `steps`.

    Search for template-type steps and render them.
    """
    rendered_steps = []
    for step in steps:
        if step['type'] != 'template':
            rendered_steps.append(step)
            continue

        # Dereference this template
        template = templates[step['template_name']]

        # Replace kwarg {slugs} with values
        interpolated_steps = _interpolate_template_kwargs(
            template=template,
            **step['kwargs'],
        )
        # 🌶️ Recurse 🌶️ into this template and look for more nested templates to
        # dereference!
        dereferenced = _deref_steps(
            steps=interpolated_steps,
            templates=templates
        )

        rendered_steps.extend(dereferenced)

    return rendered_steps


def _deref_layers(cfg: Dict[str, Any]) -> None:
    """Dereferences layers in `cfg`, modifying `cfg`.

    Expects boundaries to already be dereferenced.
    """
    datasets_config = cfg['datasets']
    for layer_config in cfg['layers']:

        # Populate related dataset configuration
        if 'dataset' not in layer_config:
            dataset_id = layer_config['input']['dataset']
            asset_id = layer_config['input']['asset']
            dataset_config = _find_in_list_by_id(datasets_config, dataset_id)
            layer_config['input']['dataset'] = dataset_config
            layer_config['input']['asset'] = dataset_config['assets'][asset_id]

        if not layer_config.get('steps'):
            # gdal remote layers and layers which require not processing have no
            # "steps"
            continue

        # Populate steps with templates where necessary
        layer_config['steps'] = _deref_steps(
            steps=layer_config['steps'],
            templates=cfg['step_templates'],
        )


def _normalize_datasets(cfg: Dict[Any, Any]) -> None:
    """Normalize dataset assets to a dict.

    Convert the list of assets into a dict keyed by asset id.
    """
    for dataset_cfg in cfg['datasets']:
        dataset_cfg['assets'] = {x['id']: copy.deepcopy(x) for x in dataset_cfg['assets']}


def _dereference_config(cfg: Dict[Any, Any]) -> Dict[Any, Any]:
    """Take a full configuration object, replace references with the referent."""
    _normalize_datasets(cfg)
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


def load_configs_from_dir(
    config_dir: Path,
    schema_fp: Path,
) -> Dict[str, Any]:
    configs: Dict[str, Any] = {}

    for config_fp in Path(config_dir).glob('*.yml'):
        cfg = _load_config(
            config_fp=config_fp,
            schema_fp=schema_fp,
        )

        # Sometimes a config file can be empty
        if not cfg:
            logger.warning(f'{config_fp} is empty!')
            continue

        configs[config_fp.stem] = cfg

    return configs


@functools.lru_cache(maxsize=None)
def make_config(*, config_dir: Path, schema_dir: Path) -> Dict[str, Any]:
    """Read all config files and dereference relationships between concepts."""
    # TODO: Avoid all this argument drilling without import cycles... this
    # shouldn't be so hard!

    # TODO: Some better solution for configs from dir...? Could be keyed by
    # filename, as in templates; in that case each file represents a "thing". Or
    # could be concatenated together for cases where each file contains a number
    # of things, and the files are just used for organization, to avoid a huge
    # unweildy file.
    cfg = {
        'project': _load_config(
            config_fp=config_dir / 'project.yml',
            schema_fp=schema_dir / 'project.yml'
        ),
        'hierarchy_settings': _load_config(
            config_fp=config_dir / 'hierarchy_settings.yml',
            schema_fp=schema_dir / 'hierarchy_settings.yml',
        ),
        # Flatten out the layer configs into a single list of layers
        'layers': list(itertools.chain.from_iterable(
            load_configs_from_dir(
                config_dir / 'layers',
                schema_dir / 'layers.yml'
            ).values()
        )),
        # Flatten out the dataset config files into a single list of datasets
        'datasets': list(itertools.chain.from_iterable(
            load_configs_from_dir(
                config_dir / 'datasets',
                schema_dir / 'datasets.yml'
            ).values()
        )),
        'step_templates': load_configs_from_dir(
            config_dir / 'step_templates',
            schema_dir / 'step_templates.yml',
        ),
    }

    return _dereference_config(cfg)


def export_config(
    cfg: Config,
    output_path: Path = DEFAULT_LAYER_MANIFEST_PATH,
) -> None:
    """Write a report to disk containing a summary of layers in config.

    This must be run after the layers are in their location, because we need to
    calculate their size on disk.
    """
    report = []
    for layer in cfg.layers.values():
        layer_type: str
        if layer.input.asset.type != 'gdal_remote':
            layer_fp = get_final_layer_filepath(layer)
            layer_dir = layer_fp.parent
            layer_size_bytes = directory_size_bytes(layer_dir)
            layer_type = vector_or_raster(layer)
        else:
            # TODO: Is there a better way to determine "vector or raster" here?
            # TODO: Expand the LayerType type to include "online"?
            layer_type = 'online'
            # online layers have no size on disk.
            layer_size_bytes = 0

        dataset_cfg = layer.input.dataset

        report.append({
            'Group': layer.hierarchy[0],
            'Subgroup': ('/'.join(layer.hierarchy[1:])),
            'Layer Title': layer.title,
            'Layer Description': layer.description,
            'Vector or Raster': layer_type,
            'Data Source Title': dataset_cfg.metadata.title,
            'Data Source Abstract': dataset_cfg.metadata.abstract,
            'Data Source Citation': dataset_cfg.metadata.citation.text,
            'Data Source Citation URL': dataset_cfg.metadata.citation.url,
            'Layer Size': naturalsize(layer_size_bytes),
            'Layer Size Bytes': layer_size_bytes,
        })

    with open(output_path, 'w') as ofile:
        # TODO: Why can't mypy infer this?
        dict_writer: csv.DictWriter = csv.DictWriter(
            ofile,
            list(report[0].keys()),
        )
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f'Exported: {os.path.abspath(ofile.name)}')
