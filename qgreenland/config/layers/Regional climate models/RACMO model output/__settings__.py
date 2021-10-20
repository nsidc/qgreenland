from qgreenland.config.helpers.layers.racmo import RACMO_LAYER_ORDER
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'layers.py:racmo_wind_vectors',
        'layers.py:racmo_wind_speed',
        *[
            f'layers.py:{layer_id}'
            for layer_id in RACMO_LAYER_ORDER
        ],
        'Supplement',
    ],
)
