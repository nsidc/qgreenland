from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'ice_cores.py:ice_cores',
        'machguth_massbalance_locations.py:machguth_massbalance_locations',
        'supraglacial_lakes.py:jakobshavn_supraglacial_lakes',
        'firn_ice.py:firn_ice_layer_thicknesses',
        'Global land ice measurements from space (GLIMS)',
        'Surface elevation change',
        'Gravimetric mass balance',
    ],
)
