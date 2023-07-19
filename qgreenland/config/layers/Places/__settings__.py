from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":towns",
        ":settlements",
        ":points_of_interest",
        ":roads",
        ":buildings",
    ],
)
