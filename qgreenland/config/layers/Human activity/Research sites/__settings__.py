from qgreenland.models.config.layer_group import LayerGroupSettings

settings = LayerGroupSettings(
    order=[
        ":gem_research_stations",
        ":promice_research_stations",
        ":promice_research_stations_former",
        ":gc_net_research_stations",
        ":seismograph_stations",
    ],
)
