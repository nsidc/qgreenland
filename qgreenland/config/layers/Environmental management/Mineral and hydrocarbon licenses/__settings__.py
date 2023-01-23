from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":mcas_mlsa_public_all",
        ":mcas_mlsa_public_historic",
    ],
)
