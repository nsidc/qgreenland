"""Provide helper functions for generating configuration.

ONLY the constants module should import this module.
"""

import csv
import hashlib
import json
import os
from pathlib import Path
from typing import Union

from humanize import naturalsize

from qgreenland._typing import VectorOrRaster
from qgreenland.models.config import Config
from qgreenland.models.config.asset import OnlineAsset
from qgreenland.util.fs import directory_contents, directory_size_bytes
from qgreenland.util.json import MagicJSONEncoder
from qgreenland.util.layer import (
    get_layer_compile_filepath,
    get_layer_release_filepath,
    vector_or_raster,
)
from qgreenland.util.tree import LayerNode, prune_layers_not_in_package


def export_config_csv(
    cfg: Config,
    *,
    output_path: Path,
    package_name: str,
) -> None:
    """Write a report to disk summarizing layers in the zip package.

    This must be run after the layers are in their location, because we need to
    calculate their size on disk.
    """
    layer_tree = prune_layers_not_in_package(
        cfg.layer_tree,
        package_name=package_name,
    )

    report = []
    for layer_node in layer_tree.leaves:
        layer_cfg = layer_node.layer_cfg

        if not layer_cfg.in_package:
            continue

        vector_or_raster_data: VectorOrRaster
        internet_required: bool

        vector_or_raster_data = vector_or_raster(layer_node)

        if isinstance(layer_cfg.input.asset, OnlineAsset):
            # Online layers have no size on disk.
            layer_size_bytes = 0
            internet_required = False
        else:
            layer_fp = get_layer_compile_filepath(
                layer_node,
                package_name=package_name,
            )
            layer_dir = layer_fp.parent
            layer_size_bytes = directory_size_bytes(layer_dir)
            internet_required = True

        dataset_cfg = layer_cfg.input.dataset

        report.append(
            {
                "Group": layer_node.group_name_path[0],
                "Subgroup": "/".join(layer_node.group_name_path[1:]),
                "Layer Title": layer_cfg.title,
                "Layer Description": layer_cfg.description,
                "Vector or Raster": vector_or_raster_data,
                "Data Source Title": dataset_cfg.metadata.title,
                "Data Source Abstract": dataset_cfg.metadata.abstract,
                "Data Source Citation": dataset_cfg.metadata.citation.text,
                "Data Source Citation URL": dataset_cfg.metadata.citation.url,
                "Layer Size": naturalsize(layer_size_bytes),
                "Layer Size Bytes": layer_size_bytes,
                "Internet Required?": internet_required,
            }
        )

    with open(output_path, "w") as ofile:
        # TODO: Why can't mypy infer this?
        dict_writer: csv.DictWriter = csv.DictWriter(
            ofile,
            list(report[0].keys()),
        )
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f"Exported: {os.path.abspath(ofile.name)}")


def export_config_json(cfg: Config) -> str:
    return json.dumps(
        cfg,
        cls=MagicJSONEncoder,
        indent=2,
        sort_keys=True,
    )


# TODO: Define model for "final" assets? Come up with a better name...
# Call them "artifacts"?
def _layer_manifest_final_assets(
    layer_node: LayerNode,
) -> list[dict[str, Union[str, int]]]:
    """List out all available finalized files on disk for this layer.

    Not to be confused with layer dataset assets, which are input files.

    TODO: Better label?
    """
    layer_cfg = layer_node.layer_cfg
    if isinstance(layer_cfg.input.asset, OnlineAsset):
        return [
            {
                "type": "online",
                **layer_cfg.input.asset.dict(
                    include={"provider", "url"},
                ),
            }
        ]
    else:
        layer_fp = get_layer_release_filepath(layer_node)
        layer_files = directory_contents(layer_fp.parent)

        return [
            {
                "file": fp.name,
                # TODO: Handle a QMD/QML next to the data
                "type": "data" if fp == layer_fp else "ancillary",
                "checksum": hashlib.md5(open(fp, "rb").read()).hexdigest(),
                "size_bytes": fp.stat().st_size,
            }
            for fp in layer_files
        ]
