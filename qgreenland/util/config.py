"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import csv
import logging
import os
from pathlib import Path

from humanize import naturalsize

from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDatasetOnlineAsset
from qgreenland.util.misc import (
    directory_size_bytes,
    get_final_layer_filepath,
    vector_or_raster,
)


logger = logging.getLogger('luigi-interface')
DEFAULT_LAYER_MANIFEST_PATH = Path('./layers.csv')


def export_config(
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
        layer_type: str
        if isinstance(layer_cfg.input.asset, ConfigDatasetOnlineAsset):
            # TODO: Is there a better way to determine "vector or raster" here?
            # TODO: Expand the LayerType type to include "online"?
            layer_type = 'online'
            # online layers have no size on disk.
            layer_size_bytes = 0
        else:
            layer_fp = get_final_layer_filepath(layer_node)
            layer_dir = layer_fp.parent
            layer_size_bytes = directory_size_bytes(layer_dir)
            layer_type = vector_or_raster(layer_node)

        dataset_cfg = layer_cfg.input.dataset

        report.append({
            # TODO:
            # 'Group': layer.hierarchy[0],
            # 'Subgroup': ('/'.join(layer.hierarchy[1:])),
            'Group': 'TODO',
            'Subgroup': 'TODO',
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
