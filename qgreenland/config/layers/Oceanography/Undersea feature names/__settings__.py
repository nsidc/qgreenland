from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("undersea_features_point"),
        LayerIdentifier("undersea_features_multilinestring"),
        LayerIdentifier("undersea_features_multipolygon"),
    ],
)
