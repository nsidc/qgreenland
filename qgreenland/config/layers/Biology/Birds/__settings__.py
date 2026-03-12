from qgreenland.config.helpers.layers.naturemap import (
    layers_cfg as naturemap_layers_cfg,
)
from qgreenland.config.helpers.layers.nunagis_protected_areas import BIRDS_LAYERS
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("caff_murre_colonies"),
        *[LayerIdentifier(layer_id) for layer_id in BIRDS_LAYERS],
        *[LayerIdentifier(layer_id) for layer_id in naturemap_layers_cfg.keys()],
    ],
)
