from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("QGreenland boundaries"),
        LayerIdentifier("arctic_circle"),
        LayerGroupIdentifier("Latitude lines"),
        LayerGroupIdentifier("Longitude lines"),
        LayerIdentifier("timezones"),
        LayerIdentifier("utm_zones"),
        LayerGroupIdentifier("Borders"),
    ],
    show=True,
    expand=True,
)
