from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'layers.py:ground_temperature',
        'layers.py:ground_temperature_sd',
        'layers.py:permafrost_probability',
    ],
)
