from qgreenland.config.helpers.layers.hotosm import hotosm_layers_order
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[f":{asset_id}" for asset_id in hotosm_layers_order()],
)
