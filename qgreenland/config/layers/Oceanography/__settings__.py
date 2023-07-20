from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Undersea feature names"),
        LayerGroupIdentifier("Seawater temperature (25km)"),
        LayerGroupIdentifier("Bathymetry"),
    ],
)
