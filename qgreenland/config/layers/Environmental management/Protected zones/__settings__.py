from qgreenland.config.helpers.layers.naturemap import PROTECTED_ZONES_LAYERS_CFG
from qgreenland.config.helpers.layers.nunagis_protected_areas import (
    PROTECTED_ZONES_LAYERS,
)
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        *[LayerIdentifier(layer_id) for layer_id in PROTECTED_ZONES_LAYERS],
        *[LayerIdentifier(layer_id) for layer_id in PROTECTED_ZONES_LAYERS_CFG.keys()],
    ],
)
