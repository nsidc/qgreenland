from qgreenland.config.datasets.woa import (
    woa_salinity,
)
from qgreenland.config.helpers.layers.woa import (
    SALINITY_COMBINATIONS,
    make_layer,
)

salinity_layers = [
    make_layer(
        dataset=woa_salinity,
        depth=depth,
        season=season,
        variable="salinity",
        units="practical salinity scale (PSS)",
    )
    for season, depth in SALINITY_COMBINATIONS
]
