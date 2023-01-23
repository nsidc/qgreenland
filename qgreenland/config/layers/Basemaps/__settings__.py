from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":land",
        ":ocean",
        ":background",
    ],
    expand=True,
    show=True,
)
