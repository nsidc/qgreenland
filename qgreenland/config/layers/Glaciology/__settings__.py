from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
    LayerIdentifier,
)

settings = LayerGroupSettings(
    order=[
        LayerIdentifier("ice_cores"),
        LayerIdentifier("machguth_massbalance_locations"),
        LayerIdentifier("jakobshavn_supraglacial_lakes"),
        LayerIdentifier("firn_ice_layer_thicknesses"),
        LayerGroupIdentifier("Glacier terminus positions 2000-2021"),
        LayerGroupIdentifier("Global land ice measurements from space (GLIMS)"),
        LayerIdentifier("ice_thickness_change"),
        LayerGroupIdentifier("Surface elevation change"),
        LayerGroupIdentifier("Gravimetric mass balance"),
        LayerGroupIdentifier("Ice sheet velocity"),
        LayerIdentifier("basal_thermal_state"),
    ],
)
