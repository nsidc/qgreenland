from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("BedMachine v5"),
        LayerGroupIdentifier("Internet required"),
    ],
)
