from qgreenland.config.helpers.layers.streams_outlets_basins import ORDERED_LAYER_IDS
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        f'layers.py:{layer_id}'
        for layer_id in ORDERED_LAYER_IDS
    ],
)