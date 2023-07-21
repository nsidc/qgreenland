from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("September (min weekly extent)"),
        LayerGroupIdentifier("Feb, March, or April (max weekly extent)"),
    ],
    expand=True,
)
