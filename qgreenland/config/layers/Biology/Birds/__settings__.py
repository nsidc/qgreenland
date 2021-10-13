from qgreenland.config.helpers.layers.nunagis_protected_areas import LAYER_IDS_ORDERED_LIST
from qgreenland.models.config.layer_group import LayerGroupSettings


settings = LayerGroupSettings(
    order=[
        'caff_murre.py:caff_common_murre_colonies',
        'caff_murre.py:caff_thickbilled_murre_colonies',
        *[
            f'nunagis_protected_areas.py:{layer_id}'
            for layer_id in LAYER_IDS_ORDERED_LIST
        ],
    ],
)
