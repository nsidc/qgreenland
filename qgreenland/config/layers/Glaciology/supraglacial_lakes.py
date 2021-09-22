from qgreenland.config.datasets.esa_cci import (
    supraglacial_lakes as dataset,
)
# from qgreenland.config.helpers.steps.build_overviews import build_overviews
# from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
# from qgreenland.models.config.step import ConfigLayerCommandStep

supraglacial_lakes = ConfigLayer(
    id='jakobshavn_supraglacial_lakes',
    title='Sermeq Kujalleq/Jakobshavn supraglacial lakes 2019',
    description="""Supraglacial lake delineation on Sermeq Kujalleq/Jakobshavn
for 2019/05/01 and 2019/10/01 generated using Sentinel-2 satellite data.""",
    tags=['water'],
    style='supraglacial_lakes',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[],
)

# MIGRATION:
# from qgreenland.config.datasets.XXXX import XXXX as dataset
# from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
#
#
# jakobshavn_supraglacial_lakes = ConfigLayer(
#     id='jakobshavn_supraglacial_lakes',
#     title='Sermeq Kujalleq/Jakobshavn supraglacial lakes 2019',
#     description=(
#         """Supraglacial lake delineation on Sermeq Kujalleq/Jakobshavn for
#         2019/05/01 and 2019/10/01 generated using Sentinel-2 satellite data."""
#     ),
#     tags=[],
#     style='XXXX',
#     input=ConfigLayerInput(
#         dataset=dataset,
#         asset=dataset.assets['XXXX'],
#     ),
#     steps=[
#     ],
# )
