from qgreenland.config.helpers.layers.racmo import RACMO_SUPPLEMENTAL_LAYER_ORDER
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        *[f":{layer_id}" for layer_id in RACMO_SUPPLEMENTAL_LAYER_ORDER],
    ],
)
