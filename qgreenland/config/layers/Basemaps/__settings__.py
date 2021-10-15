from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'ocean_shape.py:ocean',
        'background.py:background',
    ],
    expand=True,
    show=True,
)
