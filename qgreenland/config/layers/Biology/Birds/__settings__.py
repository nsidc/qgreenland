from qgreenland.config.helpers.layers.naturemap import (
    BIRDS_LAYERS_CFG as NATUREMAP_BIRDS_LAYERS_CFG,
)
from qgreenland.config.helpers.layers.nunagis_protected_areas import BIRDS_LAYERS
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("caff_murre_colonies"),
        *[LayerIdentifier(layer_id) for layer_id in BIRDS_LAYERS],
        *[LayerIdentifier(layer_id) for layer_id in NATUREMAP_BIRDS_LAYERS_CFG.keys()],
        LayerIdentifier("seabird_regulated_areas_layer"),
    ],
)
