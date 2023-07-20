from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("towns"),
        LayerIdentifier("settlements"),
        LayerIdentifier("points_of_interest"),
        LayerIdentifier("roads"),
        LayerIdentifier("buildings"),
    ],
)
