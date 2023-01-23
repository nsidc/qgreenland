from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        "QGreenland boundaries",
        ":arctic_circle",
        "Latitude lines",
        "Longitude lines",
        ":timezones",
        ":utm_zones",
        "Borders",
    ],
    show=True,
    expand=True,
)
