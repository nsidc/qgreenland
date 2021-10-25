from qgreenland.config.helpers.layers import wmm
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=wmm.wmm_layer_order(year=2025),
)
