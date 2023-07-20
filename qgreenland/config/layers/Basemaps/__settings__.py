from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("land"),
        LayerIdentifier("ocean"),
        LayerIdentifier("background"),
    ],
    expand=True,
    show=True,
)
