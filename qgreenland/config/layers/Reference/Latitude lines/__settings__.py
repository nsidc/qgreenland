from qgreenland.models.config.layer_group import LayerGroupSettings
from qgreenland.config.helpers.layers.lonlat import lonlat_ids_sorted


settings = LayerGroupSettings(
    order=[i for i in lonlat_ids_sorted if i.startswith('lat')],
)
