from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("qgr_boundary_data"),
        LayerIdentifier("qgr_boundary_background"),
    ],
    show=True,
)
