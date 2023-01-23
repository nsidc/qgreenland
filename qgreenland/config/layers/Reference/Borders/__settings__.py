from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":bas_greenland_coastlines",
        ":coastlines",
        ":nunagis_municipalities_population",
        ":ne_states_provinces",
        ":ne_countries",
    ],
    show=True,
)
