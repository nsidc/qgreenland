from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":image_mosaic_2019",
        ":image_mosaic_2015",
        ":sdfi_satellite_orthophotos",
        ":sdfi_topo_map",
        ":blue_marble_shaded_relief_bathymetry",
    ],
)
