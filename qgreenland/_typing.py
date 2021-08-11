"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Literal


ConfigStepType = Literal['command', 'python', 'template']
QgsLayerType = Literal['Vector', 'Raster']
# We're currently only bothering with "online" providers in this type...
# TODO: Rename? Add all providers, even offline?
QgsLayerProviderType = Literal['gdal', 'wms']  # TODO: ogr, wfs, wcs?
