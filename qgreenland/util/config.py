"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import csv
import logging
import os
from pathlib import Path

from humanize import naturalsize

from qgreenland._typing import QgsLayerType
from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDatasetOnlineAsset
from qgreenland.util.misc import (
    directory_size_bytes,
    get_final_layer_filepath,
    vector_or_raster,
)
from qgreenland.util.qgis.metadata import (
    build_layer_abstract,
)


logger = logging.getLogger('luigi-interface')
DEFAULT_LAYER_MANIFEST_PATH = Path('./layers.csv')


def export_config_manifest(
    cfg: Config,
    output_path: Path = DEFAULT_LAYER_MANIFEST_PATH,
) -> None:
    """Write a machine-readable manifest to disk describing available layers.

    This must be run after the layers are in their location, because we need to
    calculate their size on disk.
    """
    # json.dump()?
    # or:
    # with open(output_path, 'w') as ofile:
    #     json.dumps()
    manifest_spec_version = 'v0.1.0'
    manifest = {
        'version': manifest_spec_version,
        'qgr_version': ...,
        'layers': [{
            # ID first for readability
            'id': layer_node.layer_cfg.id,
            **layer_node.layer_cfg.dict(include={'title', 'description'}),
            'tags': ['foo', 'bar', 'baz'],
            'hierarchy': layer_node.group_name_path,
            'layer_details': build_layer_abstract(layer_node.layer_cfg),
            'assets': [], 
        } for layer_node in cfg.layer_tree.leaves],
    }
    breakpoint()
    print(manifest)
    with open(output_path, 'w') as ofile:
        json.dump(manifest, ofile)


def export_config_csv(
    cfg: Config,
    output_path: Path = DEFAULT_LAYER_MANIFEST_PATH,
) -> None:
    """Write a report to disk containing a summary of layers in config.

    This must be run after the layers are in their location, because we need to
    calculate their size on disk.
    """
    report = []
    for layer_node in cfg.layer_tree.leaves:
        layer_cfg = layer_node.layer_cfg
        layer_type: QgsLayerType
        if isinstance(layer_cfg.input.asset, ConfigDatasetOnlineAsset):
            layer_type = 'Online'
            # Online layers have no size on disk.
            layer_size_bytes = 0
        else:
            layer_fp = get_final_layer_filepath(layer_node)
            layer_dir = layer_fp.parent
            layer_size_bytes = directory_size_bytes(layer_dir)
            layer_type = vector_or_raster(layer_node)

        dataset_cfg = layer_cfg.input.dataset

        report.append({
            'Group': layer_node.group_name_path[0],
            'Subgroup': '/'.join(layer_node.group_name_path[1:]),
            'Layer Title': layer_cfg.title,
            'Layer Description': layer_cfg.description,
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
