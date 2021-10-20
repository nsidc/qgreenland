from qgreenland.config.helpers.layers.glacier_terminus import LAYER_IDS
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'glacier_terminus_ids.py:glacier_terminus_glacier_ids',
        *[
            f'glacier_terminus.py:{layer_id}'
            for layer_id in LAYER_IDS
        ],
    ],
)
