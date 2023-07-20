from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Mineral and hydrocarbon licenses"),
        LayerIdentifier("nafo_divisions"),
        LayerGroupIdentifier("Protected zones"),
        LayerGroupIdentifier("Maritime boundaries"),
    ],
)
