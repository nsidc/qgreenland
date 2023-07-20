from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("September (min monthly extent)"),
        LayerGroupIdentifier("Feb or March (max monthly extent)"),
    ],
    expand=True,
)
