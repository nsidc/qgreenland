from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from scripts.experimental.pyconfig_spike.datasets.online import (
    image_mosaic,
    sea_ice_index,
)


image_mosaic_2019 = ConfigLayer(
    id='image_mosaic_2019',
    description='Sentinel-2 multispectral satellite imagery from 2019.',
    show=False,
    in_package=True,
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
    show=False,
    in_package=True,
    input=ConfigLayerInput(
      dataset=sea_ice_index,
      asset=sea_ice_index.assets['monthly_polyline_n'],
    ),
)
