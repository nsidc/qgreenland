from qgreenland.config.helpers.layers.territorial_waters import (
    LAYER_PARAMS as TERRITORIAL_WATERS_PARAMS,
)
from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        *[LayerIdentifier(layer_id) for layer_id in TERRITORIAL_WATERS_PARAMS.keys()],
        LayerGroupIdentifier("Continental shelf"),
    ],
)
