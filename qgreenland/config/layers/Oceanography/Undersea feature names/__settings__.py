from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        ':undersea_features_point',
        ':undersea_features_multilinestring',
        ':undersea_features_multipolygon',
    ],
)
