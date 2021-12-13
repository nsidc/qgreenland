from qgreenland.config.helpers.layers.territorial_waters import LAYER_PARAMS as TERRITORIAL_WATERS_PARAMS
from qgreenland.config.helpers.layers.continental_shelf import LAYER_PARAMS as CONTINENTAL_SHELF_PARAMS
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        *[f':{layer_id}' for layer_id in TERRITORIAL_WATERS_PARAMS.keys()],
        *[f':{layer_id}' for layer_id in CONTINENTAL_SHELF_PARAMS.keys()],
    ],
)
