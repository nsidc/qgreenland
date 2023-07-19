from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":gem_research_stations",
        ":promice_gc_net_stations",
        ":seismograph_stations",
    ],
)
