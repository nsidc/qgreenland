from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

settings = LayerGroupSettings(
    order=[
        LayerIdentifier(layer_id)
        for layer_id in (
            "velocity_mosaic",
            "velocity_mosaic_error",
            "velocity_mosaic_ice_mask",
        )
    ],
)
