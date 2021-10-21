from qgreenland.config.helpers.layers.woa2018 import WOA2018_LAYER_ORDER
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        *[
            f':{layer_id}'
            for layer_id in WOA2018_LAYER_ORDER
        ],
    ],
)
