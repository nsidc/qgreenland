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
from qgreenland.util.fs import directory_contents, directory_size_bytes
from qgreenland.util.json import MagicJSONEncoder
from qgreenland.util.layer import (
    get_layer_compile_filepath,
    get_layer_release_filepath,
    vector_or_raster,
)
from qgreenland.util.metadata import build_layer_metadata
from qgreenland.util.tree import LayerNode
from qgreenland.util.version import get_build_version

DEFAULT_LAYER_MANIFEST_PATH = Path("./layers.csv")


def export_config_manifest(
    cfg: Config,
    output_path: Path = DEFAULT_LAYER_MANIFEST_PATH,
) -> None:
    """Write a machine-readable manifest to disk describing available layers.

    This includes layers for which `in_package is False`.

    This must be run after the layers are in their release location, because we
    need to calculate their size on disk.
    """
    manifest_spec_version = "v0.1.0"
    manifest = {
        "version": manifest_spec_version,
        "qgr_version": get_build_version(),
        "layers": [
            {
                # ID first for readability
                "id": layer_node.layer_cfg.id,
                **layer_node.layer_cfg.dict(include={"title", "description", "tags"}),
                "hierarchy": layer_node.group_name_path,
                "layer_details": build_layer_metadata(layer_node.layer_cfg),
                "assets": _layer_manifest_final_assets(layer_node),
            }
            for layer_node in cfg.layer_tree.leaves
            # For now, do not include online layers in the layer manifest. The
            # `QGreenland Custom` QGIS Plugin does not currently support online
            # layers. Once online layers are supported in the plugin, this `if`
            # statement can be removed.
            if not layer_node.layer_cfg.is_online_only
        ],
    }

    with open(output_path, "w") as ofile:
        json.dump(manifest, ofile)


def export_config_csv(
    cfg: Config,
    output_path: Path = DEFAULT_LAYER_MANIFEST_PATH,
) -> None:
    """Write a report to disk summarizing layers in the zip package.

    This must be run after the layers are in their location, because we need to
    calculate their size on disk.
    """
    report = []
    for layer_node in cfg.layer_tree.leaves:
        layer_cfg = layer_node.layer_cfg

        if not layer_cfg.in_package:
            continue

        vector_or_raster_data: VectorOrRaster
        internet_required: bool

        vector_or_raster_data = vector_or_raster(layer_node)

        if layer_cfg.is_online_only:
            # Online layers have no size on disk.
            layer_size_bytes = 0
            internet_required = False
        else:
            layer_fp = get_layer_compile_filepath(layer_node)
            layer_dir = layer_fp.parent
            layer_size_bytes = directory_size_bytes(layer_dir)
            internet_required = True

        # TODO: re-consider how these records are exported when a layer is
        # derived from multiple inputs.
        data_source_titles = ""
        data_source_abstracts = ""
        data_source_citations = ""
        data_source_citation_urls = ""
        for layer_input in layer_cfg.inputs:
            dataset_cfg = layer_input.dataset

            data_source_titles += dataset_cfg.metadata.title + ";"
            data_source_abstracts += dataset_cfg.metadata.abstract + ";"
            data_source_citations += dataset_cfg.metadata.citation.text + ";"
            data_source_citation_urls += dataset_cfg.metadata.citation.url + ";"

        report.append(
            {
                "Group": layer_node.group_name_path[0],
                "Subgroup": "/".join(layer_node.group_name_path[1:]),
                "Layer Title": layer_cfg.title,
                "Layer Description": layer_cfg.description,
                "Vector or Raster": vector_or_raster_data,
                "Data Source Title(s)": data_source_titles,
                "Data Source Abstract(s)": data_source_abstracts,
                "Data Source Citation(s)": data_source_citations,
                "Data Source Citation URL(s)": data_source_citation_urls,
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
    if online_asset := layer_cfg.online_only_asset:
        return [
            {
                "type": "online",
                **online_asset.dict(
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
