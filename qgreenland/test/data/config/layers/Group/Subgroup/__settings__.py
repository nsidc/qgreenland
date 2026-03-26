from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("example_vector"),
        LayerIdentifier("example_online"),
        LayerIdentifier("example_raster"),
        LayerGroupIdentifier("Subgroup2"),
    ],
)
