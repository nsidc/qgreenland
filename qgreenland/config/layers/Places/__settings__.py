from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":populated_places",
        ":comprehensive_places",
        ":buildings",
        ":roads",
    ],
)
