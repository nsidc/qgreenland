from qgreenland.config.helpers.layers.racmo import RACMO_LAYER_ORDER
from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        *[f":{layer_id}" for layer_id in RACMO_LAYER_ORDER],
        LayerGroupIdentifier("Supplement"),
    ],
)
