from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("populated_places"),
        LayerIdentifier("points_of_interest"),
        LayerIdentifier("roads"),
        LayerIdentifier("buildings"),
    ],
)
