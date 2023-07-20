from qgreenland.config.helpers.layers.nunagis_protected_areas import BIRDS_LAYERS
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("caff_common_murre_colonies"),
        LayerIdentifier("caff_thickbilled_murre_colonies"),
        *[f":{layer_id}" for layer_id in BIRDS_LAYERS],
    ],
)
