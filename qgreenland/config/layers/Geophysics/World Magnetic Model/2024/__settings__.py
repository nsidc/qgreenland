from qgreenland.config.helpers.layers import wmm
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=wmm.wmm_layer_order(layer_filename='layers.py', year=2024),
)
