from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        'Dip poles',
        'Geomagnetic coordinates 2020',
        *[str(year) for year in range(2020, 2025 + 1)]
    ],
)
