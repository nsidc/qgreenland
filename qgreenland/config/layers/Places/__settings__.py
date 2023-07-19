from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":comprehensive_places",
        ":buildings",
        ":roads",
        ":cities",
        ":settlements",
    ],
)
