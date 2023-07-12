from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":earthquakes",
        ":tectonic_plate_boundaries",
        ":tectonic_plate_polygons",
        ":soil_types",
        "Geological map",
    ],
)
