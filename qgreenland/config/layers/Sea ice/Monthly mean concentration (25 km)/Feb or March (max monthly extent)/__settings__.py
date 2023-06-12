from qgreenland.config.helpers.layers.sea_ice_concentration import (
    MAX_CONCENTRATION_YEARS,
)
from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[f":seaice_maximum_concentration_{year}" for year in MAX_CONCENTRATION_YEARS],
)
