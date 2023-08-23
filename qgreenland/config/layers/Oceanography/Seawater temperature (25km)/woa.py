from qgreenland.config.datasets.woa import (
    woa_temperature,
)
from qgreenland.config.helpers.layers.woa import TEMPERATURE_COMBINATIONS, make_layer

temperature_layers = [
    make_layer(
        dataset=woa_temperature,
        depth=depth,
        season=season,
        variable="temperature",
        units="°C",
    )
    for season, depth in TEMPERATURE_COMBINATIONS
]
