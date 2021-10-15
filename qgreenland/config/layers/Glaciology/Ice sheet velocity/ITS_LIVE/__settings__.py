from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        f'layers.py:{layer_id}'
        for layer_id in (
            'velocity_mosaic',
            'velocity_mosaic_error',
            'velocity_mosaic_ice_mask',
        )
    ],
)
