from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'coastlines.py:bas_greenland_coastlines',
        'coastlines.py:coastlines',
        'political_boundaries.py:nunagis_municipalities_population',
        'political_boundaries.py:ne_states_provinces',
        'political_boundaries.py:ne_countries',
    ],
    show=True,
)
