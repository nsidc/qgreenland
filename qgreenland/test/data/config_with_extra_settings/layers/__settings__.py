from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerIdentifier,
    RootGroupSettings,
)

settings = RootGroupSettings(
    order=[
        LayerGroupIdentifier("Group"),
        LayerIdentifier("extra_layer"),
        LayerGroupIdentifier("Extra group"),
    ],
)
