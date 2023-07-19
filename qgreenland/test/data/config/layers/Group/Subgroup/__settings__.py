from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("example_online"),
        LayerIdentifier("example_raster"),
    ],
)
