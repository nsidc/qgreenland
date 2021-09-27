from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.sea_ice_concentration import (
    CONCENTRATION_DESCRIPTION,
    CONCENTRATION_STYLE,
    CONCENTRATION_YEARS,
)
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


layers = [
    ConfigLayer(
        id=f'seaice_minimum_concentration_{year}',
        title=f'September {year}',
        description=CONCENTRATION_DESCRIPTION,
        tags=[],
        style=CONCENTRATION_STYLE,
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'minimum_concentration_{year}'],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'gdal_calc.py',
                    '--calc', "'A / 10.0'",
                    '-A', '{input_dir}/*.tif',
                    '--outfile={output_dir}/downscaled.tif',
                ],
            ),
            ConfigLayerCommandStep(
                args=[
                    'foo',
                ],
            ),
        ],
    ) for year in CONCENTRATION_YEARS
]
