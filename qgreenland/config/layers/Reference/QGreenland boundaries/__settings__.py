from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'qgr_boundaries.py:qgr_boundary_data',
        'qgr_boundaries.py:qgr_boundary_background',
    ],
    show=True,
)
