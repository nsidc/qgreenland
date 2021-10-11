from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'borders.py:bas_greenland_coastlines',
        'borders.py:coastlines',
    ],
    show=True,
)
