from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("geothermal_heat_flow_measurements"),
        LayerIdentifier("geothermal_heat_flow_map"),
    ],
)
