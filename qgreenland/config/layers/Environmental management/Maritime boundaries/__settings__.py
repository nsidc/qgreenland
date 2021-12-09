from qgreenland.config.helpers.layers.territorial_waters import (
    LAYER_PARAMS as territorial_waters_layers,
)
from qgreenland.config.helpers.layers.continental_shelf import (
    LAYER_PARAMS as continental_shelf_layers,
)
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        f':{layer_id}' for
        layer_id in territorial_waters_layers.keys() for
        asset_id in continental_shelf_layers.keys()
    ],
)
