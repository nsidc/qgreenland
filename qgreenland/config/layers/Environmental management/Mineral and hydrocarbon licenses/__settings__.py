from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("mcas_mlsa_public_all"),
        LayerIdentifier("mcas_mlsa_public_historic"),
    ],
)
