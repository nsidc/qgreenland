from qgreenland.config.helpers.layers.naturemap import make_protected_zones_layers
from qgreenland.config.helpers.layers.nunagis_protected_areas import (
    PROTECTED_ZONES_LAYERS,
    make_layers,
)

layers = make_layers(PROTECTED_ZONES_LAYERS)

naturemap_layers = make_protected_zones_layers()
