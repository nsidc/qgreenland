from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("sdfi_topo_map"),
        LayerIdentifier("blue_marble_shaded_relief_bathymetry"),
    ],
)
