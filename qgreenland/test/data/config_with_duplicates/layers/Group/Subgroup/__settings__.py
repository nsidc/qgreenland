from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("example_vector"),
        LayerGroupIdentifier("Foo"),
        LayerIdentifier("example_online"),
        LayerGroupIdentifier("Baz"),
        LayerGroupIdentifier("Bar"),
        LayerIdentifier("example_raster"),
    ],
)
