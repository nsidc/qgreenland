from qgreenland.config.helpers.layers.streams_outlets_basins import ORDERED_LAYER_IDS
from qgreenland.models.config.layer_group import (
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        *[LayerIdentifier(layer_id) for layer_id in ORDERED_LAYER_IDS],
    ],
)
