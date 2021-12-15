from qgreenland.config.helpers.layers.territorial_waters import LAYER_PARAMS as TERRITORIAL_WATERS_PARAMS
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        *[f':{layer_id}' for layer_id in TERRITORIAL_WATERS_PARAMS.keys()],
        'Continental shelf',
    ],
)
