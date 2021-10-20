from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'undersea_features.py:undersea_features_point',
        'undersea_features.py:undersea_features_multilinestring',
        'undersea_features.py:undersea_features_multipolygon',
    ],
)