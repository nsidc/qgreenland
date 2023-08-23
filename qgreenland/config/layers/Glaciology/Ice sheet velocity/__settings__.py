from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("GrIMP"),
        LayerGroupIdentifier("ITS_LIVE"),
        LayerGroupIdentifier("ESA Climate Change Initiative"),
    ],
)
