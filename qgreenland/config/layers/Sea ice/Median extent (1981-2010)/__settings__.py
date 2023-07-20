from qgreenland.config.helpers.layers.seaice import layer_id
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[LayerIdentifier(layer_id(month)) for month in range(1, 12 + 1)],
)
