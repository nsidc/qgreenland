from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        ':ice_cores',
        ':machguth_massbalance_locations',
        ':jakobshavn_supraglacial_lakes',
        ':firn_ice_layer_thicknesses',
        'Glacier terminus positions 2000-2017',
        'Global land ice measurements from space (GLIMS)',
        ':ice_thickness_change',
        'Surface elevation change',
        'Gravimetric mass balance',
        'Ice sheet velocity',
        ':basal_thermal_state',
    ],
)
