from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'online.py:image_mosaic_2019',
        'online.py:image_mosaic_2015',
        # TODO: why is this layer failing?
        #   `Invalid QgsMapLayer created for layer g02135_polyline_n`
        # 'online.py:g02135_polyline_n',
    ],
)
