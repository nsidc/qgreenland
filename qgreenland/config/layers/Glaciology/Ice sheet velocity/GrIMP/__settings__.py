from qgreenland.models.config.layer_group import (
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("grimp_annual_vectors_2021"),
        LayerIdentifier("grimp_annual_vv_2021"),
        LayerIdentifier("grimp_annual_vx_2021"),
        LayerIdentifier("grimp_annual_vy_2021"),
    ],
)
