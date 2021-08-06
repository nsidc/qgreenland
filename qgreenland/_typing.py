"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Literal, Union

import qgis.core as qgc


ConfigStepType = Literal['command', 'python', 'template']

AnyQgsLayer = Union[qgc.QgsVectorLayer, qgc.QgsRasterLayer]
