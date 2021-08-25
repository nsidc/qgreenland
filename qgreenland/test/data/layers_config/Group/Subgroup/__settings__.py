from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order = [
        'Foo',
        'examples.py:example_online',
        'Baz',
        'Bar',
        'examples.py:example_raster',
    ],
)
