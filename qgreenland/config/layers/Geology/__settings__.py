from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Internet required"),
        LayerIdentifier("earthquakes"),
        LayerIdentifier("tectonic_plate_boundaries"),
        LayerIdentifier("tectonic_plate_polygons"),
        LayerIdentifier("mineral_occurrences"),
        LayerIdentifier("soil_types"),
        LayerGroupIdentifier("Geological map"),
    ],
)
