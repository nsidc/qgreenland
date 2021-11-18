from qgreenland.config.helpers.layers.lonlat import lonlat_ids_sorted
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[f':{i}' for i in lonlat_ids_sorted if i.startswith('lon')],
)
