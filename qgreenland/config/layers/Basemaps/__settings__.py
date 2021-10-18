from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'land_ocean_shape.py:land',
        'land_ocean_shape.py:ocean',
        'background.py:background',
    ],
    expand=True,
    show=True,
)
