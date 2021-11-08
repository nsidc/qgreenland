from qgreenland.config.helpers.layers.geological_map import LAYER_PARAMS
from qgreenland.config.helpers.layers.geological_map import make_layer

layers = [
    make_layer(layer_id=key, layer_params=params)
    for key, params in LAYER_PARAMS.items()
]
