from qgreenland.config.helpers.layers.woa import WOA_LAYER_ORDER
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        *[f":{layer_id}" for layer_id in WOA_LAYER_ORDER],
    ],
)
