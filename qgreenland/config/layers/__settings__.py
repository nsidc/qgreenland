from qgreenland.models.config.layer_group import LayerGroupIdentifier, RootGroupSettings

settings = RootGroupSettings(
    order=[
        LayerGroupIdentifier("Reference"),
        LayerGroupIdentifier("Places"),
        LayerGroupIdentifier("Human activity"),
        LayerGroupIdentifier("Biology"),
        LayerGroupIdentifier("Environmental management"),
        LayerGroupIdentifier("Regional climate models"),
        LayerGroupIdentifier("Frozen ground"),
        LayerGroupIdentifier("Glaciology"),
        LayerGroupIdentifier("Geology"),
        LayerGroupIdentifier("Geophysics"),
        LayerGroupIdentifier("Hydrology"),
        LayerGroupIdentifier("Sea ice"),
        LayerGroupIdentifier("Oceanography"),
        LayerGroupIdentifier("Future projections"),
        LayerGroupIdentifier("Terrain models"),
        LayerGroupIdentifier("Satellite imagery (Internet required)"),
        LayerGroupIdentifier("Basemaps"),
    ],
)
