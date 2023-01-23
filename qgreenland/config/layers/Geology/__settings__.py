from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":earthquakes",
        ":tectonic_plate_boundaries",
        ":soil_types",
        "Geological map",
    ],
)
