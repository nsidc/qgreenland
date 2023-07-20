from qgreenland.config.helpers.layers.sea_ice_age import seaice_age_layers
from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier(f"seaice_minimum_age_{year}")
        for year in seaice_age_layers.keys()
    ],
)
