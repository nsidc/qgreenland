from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("seal_tag_measurements"),
        LayerGroupIdentifier("Undersea feature names"),
        LayerGroupIdentifier("Seawater temperature (25km)"),
        LayerGroupIdentifier("Seawater salinity (25km)"),
        LayerGroupIdentifier("Bathymetry"),
    ],
)
