from pathlib import Path

import qgreenland.exceptions as exc
from qgreenland._typing import VectorOrRaster
from qgreenland.constants.misc import PROVIDER_VECTOR_OR_RASTER_MAPPING
from qgreenland.constants.paths import RELEASE_LAYERS_DIR
from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.layer import Layer
from qgreenland.util.fs import get_layer_fp
from qgreenland.util.misc import compile_package_dir
from qgreenland.util.tree import LayerNode


def vector_or_raster(
    layer_node: LayerNode,
) -> VectorOrRaster:
    layer_cfg = layer_node.layer_cfg
    if type(layer_cfg.input.asset) is OnlineAsset:
        return PROVIDER_VECTOR_OR_RASTER_MAPPING[layer_cfg.input.asset.provider]
    else:
        layer_path = get_layer_release_filepath(layer_node)
        return _vector_or_raster_from_fp(layer_path)


def get_layer_compile_dir(
    layer_node: LayerNode,
    *,
    package_name: str,
) -> Path:
    """Get the layer directory in package compilation location."""
    layer_group_path_str = "/".join(layer_node.group_name_path)
    return (
        compile_package_dir(package_name)
        / layer_group_path_str
        / _layer_dirname_from_cfg(layer_node.layer_cfg)
    )


def get_layer_release_dir(
    layer_node: LayerNode,
) -> Path:
    return RELEASE_LAYERS_DIR / layer_node.layer_cfg.id


def datasource_dirname(*, dataset_id: str, asset_id: str) -> str:
    return f"{dataset_id}.{asset_id}"


def get_layer_compile_filepath(layer_node: LayerNode, *, package_name: str) -> Path:
    return get_layer_fp(
        get_layer_compile_dir(
            layer_node,
            package_name=package_name,
        )
    )


def get_layer_release_filepath(
    layer_node: LayerNode,
) -> Path:
    return get_layer_fp(get_layer_release_dir(layer_node))


def _layer_dirname_from_cfg(layer_cfg: Layer) -> str:
    return layer_cfg.title


def _vector_or_raster_from_fp(fp: Path) -> VectorOrRaster:
    if fp.suffix == ".tif":
        return "Raster"
    elif fp.suffix == ".gpkg":
        return "Vector"
    else:
        raise exc.QgrQgsLayerError(
            f"Unexpected extension: {fp}. Expected .tif or .gpkg.",
        )
