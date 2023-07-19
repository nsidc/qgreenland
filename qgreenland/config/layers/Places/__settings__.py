from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":cities",
        ":settlements",
        ":comprehensive_places",
        ":roads",
        ":buildings",
    ],
)
