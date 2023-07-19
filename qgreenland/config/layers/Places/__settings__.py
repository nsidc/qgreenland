from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":buildings",
        ":roads",
        ":cities",
        ":settlements",
        ":comprehensive_places",
    ],
)
