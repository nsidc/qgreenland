from qgreenland.config.helpers.layers.nunagis_protected_areas import BIRDS_LAYERS
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("caff_murre_colonies"),
        *[LayerIdentifier(layer_id) for layer_id in BIRDS_LAYERS],
        LayerIdentifier("barnacle_goose_colony"),
        LayerIdentifier("goose_moulting_and_breeding_areas"),
    ],
)
