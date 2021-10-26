from qgreenland.config.datasets.online import (
    image_mosaic,
    sea_ice_index,
)
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


image_mosaic_layers = [
    ConfigLayer(
        id=f'image_mosaic_{year}',
        title=f'Greenland image mosaic {year} ({resolution}m)',
        description=f'Sentinel-2 multispectral satellite imagery from {year}.',
        tags=['online'],
        style='transparent_rgb',
        input=ConfigLayerInput(
            dataset=image_mosaic,
            asset=image_mosaic.assets[year],
        ),
    )

    for year, resolution in (('2015', '15'), ('2019', '10'))
]


g02135_polyline_n = ConfigLayer(
    id='g02135_polyline_n',
    title='Monthly sea ice extent (1979 - present)',
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
