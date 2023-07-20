from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("bas_greenland_coastlines"),
        LayerIdentifier("coastlines"),
        LayerIdentifier("nunagis_municipalities_population"),
        LayerIdentifier("ne_states_provinces"),
        LayerIdentifier("ne_countries"),
    ],
    show=True,
)
