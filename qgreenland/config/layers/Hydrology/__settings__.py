from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("marginal_lakes"),
        LayerGroupIdentifier("Streams, outlets, and basins"),
    ],
)
