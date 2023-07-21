from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Median extent (1981-2010)"),
        LayerGroupIdentifier("Weekly age (12.5km)"),
        LayerGroupIdentifier("Monthly mean concentration (25 km)"),
    ],
)
