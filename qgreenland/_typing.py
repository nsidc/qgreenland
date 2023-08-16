"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Literal, Union

VectorOrRaster = Literal["Vector", "Raster"]
QgsLayerProviderType = Literal["gdal", "ogr", "wms", "wfs", "wcs"]

ResamplingMethod = Literal["bilinear", "nearest"]

# We don't use Sequence because `isinstance('', Sequence)`
StepArgs = Union[tuple, list]
