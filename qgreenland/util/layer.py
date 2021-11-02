from pathlib import Path

import qgreenland.exceptions as exc
from qgreenland._typing import QgsLayerType
from qgreenland.constants import (
    PROVIDER_LAYERTYPE_MAPPING,
    TaskType,
)
from qgreenland.models.config.asset import ConfigDatasetOnlineAsset
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.fs import get_layer_fp
from qgreenland.util.tree import LayerNode


def vector_or_raster(layer_node: LayerNode) -> QgsLayerType:
    layer_cfg = layer_node.layer_cfg
    if type(layer_cfg.input.asset) is ConfigDatasetOnlineAsset:
        return PROVIDER_LAYERTYPE_MAPPING[layer_cfg.input.asset.provider]
    else:
        layer_path = get_final_layer_filepath(layer_node)
        return _vector_or_raster_from_fp(layer_path)


def get_final_layer_dir(
    layer_node: LayerNode,
) -> Path:
    """Get the layer directory in its final pre-zip location."""
    layer_group_path_str = '/'.join(layer_node.group_name_path)
    return (
        Path(TaskType.FINAL.value)
        / layer_group_path_str
        / _layer_dirname_from_cfg(layer_node.layer_cfg)
    )


def datasource_dirname(*, dataset_id: str, asset_id: str) -> str:
    return f'{dataset_id}.{asset_id}'


def get_final_layer_filepath(
    layer_node: LayerNode,
) -> Path:
    d = get_final_layer_dir(layer_node)
    layer_fp = get_layer_fp(d)

    if not layer_fp.is_file():
        raise exc.QgrRuntimeError(f"Layer located at '{layer_fp}' does not exist.")

    return layer_fp


def _layer_dirname_from_cfg(layer_cfg: ConfigLayer) -> str:
    return layer_cfg.title


def _vector_or_raster_from_fp(fp: Path) -> QgsLayerType:
    if fp.suffix == '.tif':
        return 'Raster'
    elif fp.suffix == '.gpkg':
        return 'Vector'
    else:
        raise exc.QgrQgsLayerError(
            f'Unexpected extension: {fp}. Expected .tif or .gpkg.',
        )
