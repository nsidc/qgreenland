from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Internet required"),
        LayerIdentifier("land"),
        LayerIdentifier("ocean"),
        LayerIdentifier("background"),
    ],
    expand=True,
    show=True,
)
