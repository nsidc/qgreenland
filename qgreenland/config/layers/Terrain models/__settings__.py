from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("BedMachine"),
        LayerIdentifier("arctic_dem"),
    ],
)
