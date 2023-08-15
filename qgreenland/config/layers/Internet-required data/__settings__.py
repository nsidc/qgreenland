from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("image_mosaic_2019"),
        LayerIdentifier("image_mosaic_2015"),
        LayerIdentifier("sdfi_satellite_orthophotos"),
        LayerIdentifier("sdfi_topo_map"),
        LayerIdentifier("geus_geological_map"),
        LayerIdentifier("blue_marble_shaded_relief_bathymetry"),
    ],
)
