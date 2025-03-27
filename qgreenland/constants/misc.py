from qgreenland._typing import QgsLayerProviderType, VectorOrRaster

PROVIDER_VECTOR_OR_RASTER_MAPPING: dict[QgsLayerProviderType, VectorOrRaster] = {
    "gdal": "Raster",
    "wms": "Raster",
    "wfs": "Vector",
    "arcgismapserver": "Raster",
}
