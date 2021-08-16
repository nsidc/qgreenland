"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Literal


QgsLayerType = Literal['Vector', 'Raster']
QgsLayerProviderType = Literal['gdal', 'ogr', 'wms', 'wfs', 'wcs']
