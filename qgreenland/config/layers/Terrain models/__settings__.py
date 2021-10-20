from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'BedMachine',
        'arctic_dem.py:arctic_dem',
        'dms_gtk_topo.py:dms_gtk_topo',
    ],
)
