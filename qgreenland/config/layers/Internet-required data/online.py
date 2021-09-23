from qgreenland.config.datasets.online import (
    image_mosaic,
    sea_ice_index,
)
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


image_mosaic_2019 = ConfigLayer(
    id='image_mosaic_2019',
    title='Greenland image mosaic 2019 (10m)',
    description='Sentinel-2 multispectral satellite imagery from 2019.',
    tags=['online'],
    style='transparent_rgb',
    input=ConfigLayerInput(
        dataset=image_mosaic,
        asset=image_mosaic.assets['2019'],
    ),

)
g02135_polyline_n = ConfigLayer(
    id='g02135_polyline_n',
    title='Sea Ice Index',
    style='g02135_polyline_n',
    description="""
Lines representing monthly sea ice extent edges. Note that aside from 2016 to
present, most of the data is missing.""",
    tags=['online'],
    input=ConfigLayerInput(
        dataset=sea_ice_index,
        asset=sea_ice_index.assets['monthly_polyline_n'],
    ),
)
