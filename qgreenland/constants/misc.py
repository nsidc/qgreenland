from qgreenland._typing import (
    QgsLayerProviderType,
    QgsLayerType,
)


PROVIDER_LAYERTYPE_MAPPING: dict[QgsLayerProviderType, QgsLayerType] = {
    'gdal': 'Raster',
    'wms': 'Raster',
    'wfs': 'Vector',
}
