from qgreenland.config.helpers.layers.woa import WOA_LAYER_ORDER
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        *[LayerIdentifier(layer_id) for layer_id in WOA_LAYER_ORDER],
    ],
)
