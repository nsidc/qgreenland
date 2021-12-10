from qgreenland.config.helpers.layers.territorial_waters import LAYER_PARAMS
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        *[f':{layer_id}' for layer_id in LAYER_PARAMS.keys()],
    ],
)
