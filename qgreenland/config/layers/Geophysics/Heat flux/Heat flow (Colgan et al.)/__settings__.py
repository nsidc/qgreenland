from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":geothermal_heat_flow_measurements",
        ":geothermal_heat_flow_map",
    ],
)
