from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'QGreenland boundaries',
        'Latitude lines',
        'Longitude lines',
        'timezones.py:timezones',
        'utm_zones.py:utm_zones',
        'Borders',
    ],
    show=True,
    expand=True,
)
