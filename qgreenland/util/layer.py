import os
from pathlib import Path

import qgreenland.exceptions as exc
from qgreenland._typing import VectorOrRaster
from qgreenland.constants.misc import PROVIDER_VECTOR_OR_RASTER_MAPPING
from qgreenland.constants.paths import COMPILE_PACKAGE_DIR, RELEASE_LAYERS_DIR
from qgreenland.models.config.layer import Layer
from qgreenland.util.config.config import get_config
from qgreenland.util.fs import get_layer_fp
from qgreenland.util.tree import LayerNode, leaf_lookup


def vector_or_raster(layer_node: LayerNode) -> VectorOrRaster:
    layer_cfg = layer_node.layer_cfg
    if online_asset := layer_cfg.online_only_asset:
        return PROVIDER_VECTOR_OR_RASTER_MAPPING[online_asset.provider]
    else:
        layer_path = get_layer_compile_filepath(layer_node)
        return _vector_or_raster_from_fp(layer_path)


def get_layer_compile_dir(
    layer_node: LayerNode,
) -> Path:
    """Get the layer directory in package compilation location."""
    layer_group_path_str = "/".join(layer_node.group_name_path)
    return (
        COMPILE_PACKAGE_DIR
        / layer_group_path_str
        / _layer_dirname_from_cfg(layer_node.layer_cfg)
    )


def get_layer_release_dir(
    layer_node: LayerNode,
) -> Path:
    return RELEASE_LAYERS_DIR / layer_node.layer_cfg.id


def datasource_dirname(*, dataset_id: str, asset_id: str) -> str:
    return f"{dataset_id}.{asset_id}"


def get_layer_compile_filepath(
    layer_node: LayerNode,
) -> Path:
    return get_layer_fp(get_layer_compile_dir(layer_node))


def get_layer_release_filepath(
    layer_node: LayerNode,
) -> Path:
    return get_layer_fp(get_layer_release_dir(layer_node))


def _layer_dirname_from_cfg(layer_cfg: Layer) -> str:
    return layer_cfg.title


def _vector_or_raster_from_fp(fp: Path) -> VectorOrRaster:
    if fp.suffix == ".tif":
        return "Raster"
    elif fp.suffix == ".gpkg" or fp.suffix == ".vrt":
        return "Vector"
    else:
        raise exc.QgrQgsLayerError(
            f"Unexpected extension: {fp}. Expected .tif or .gpkg.",
        )


def get_layer_node_for_id(layer_id: str):
    config = get_config()
    return leaf_lookup(config.layer_tree, target_node_name=layer_id)


def get_layer_cfg_for_id(layer_id: str):
    config = get_config()
    return config.layers[layer_id]


def get_vrt_rel_ref_data_dir(*, reference_node: LayerNode, vrt_node: LayerNode) -> Path:
    rel_reference_data_dir = Path(
        os.path.relpath(
            get_layer_compile_dir(reference_node),
            get_layer_compile_dir(vrt_node),
        )
    )

    return rel_reference_data_dir


# TODO: rename to something like `get_vrt_referenced_layer_data_relpath`?
def get_vrt_referenced_layer_relpath(layer_cfg: Layer) -> Path | None:
    """Given a VRT layer config, return the relative path to the referenced data.

    Returns None if the layer is not a vrt layer.
    """
    referenced_layer_id = layer_cfg.vrt_layer_ref_id
    if referenced_layer_id is None:
        return None

    referenced_data_node = get_layer_node_for_id(referenced_layer_id)
    this_node = get_layer_node_for_id(layer_cfg.id)

    rel_reference_data_dir = get_vrt_rel_ref_data_dir(
        reference_node=referenced_data_node,
        vrt_node=this_node,
    )

    reference_data_fn = get_layer_fp(get_layer_release_dir(referenced_data_node)).name

    rel_reference_data_fp = rel_reference_data_dir / reference_data_fn

    return rel_reference_data_fp


def get_layer_path_by_id(layer_id: str) -> str:
    """Return a str representing the layer path.

    E.g., "Reference/Borders/Greenland municipalities"
    """
    layer_cfg = get_layer_cfg_for_id(layer_id)
    node = get_layer_node_for_id(layer_cfg.id)
    group_path = "/".join(node.group_name_path)
    layer_path = group_path + f"/{layer_cfg.title}"

    return layer_path
