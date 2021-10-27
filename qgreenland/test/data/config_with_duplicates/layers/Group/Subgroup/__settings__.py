from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        'Foo',
        ':example_online',
        'Baz',
        'Bar',
        ':example_raster',
    ],
)
