from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("cryo_seismic_events"),
        LayerIdentifier("earthquakes"),
        LayerIdentifier("tectonic_plate_boundaries"),
        LayerIdentifier("tectonic_plate_polygons"),
        LayerIdentifier("soil_types"),
        LayerGroupIdentifier("Geological map"),
    ],
)
