from qgreenland.models.config.layer_group import (
    LayerGroupIdentifier,
    LayerGroupSettings,
)

settings = LayerGroupSettings(
    order=[
        LayerGroupIdentifier("Geomagnetic north pole"),
        LayerGroupIdentifier("Geomagnetic coordinates 2020"),
        *[str(year) for year in range(2020, 2025 + 1)],
    ],
)
