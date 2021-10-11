from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'coastlines.py:bas_greenland_coastlines',
        'coastlines.py:coastlines',
    ],
    show=True,
)
