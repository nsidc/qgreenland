from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("gem_research_stations"),
        LayerIdentifier("promice_gc_net_stations"),
        LayerIdentifier("seismograph_stations"),
    ],
)
