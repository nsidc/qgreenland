import calendar

from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.sea_ice_concentration import (
    conc_max_month,
    CONCENTRATION_DESCRIPTION,
    CONCENTRATION_STYLE,
    CONCENTRATION_YEARS,
)
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _layer(year) -> ConfigLayer:
    month = conc_max_month(year)
    month_name = calendar.month_name[month]

    return ConfigLayer(
        id=f'seaice_maximum_concentration_{year}',
        title=f'{month_name} {year}',
        description=CONCENTRATION_DESCRIPTION,
        tags=[],
        style=CONCENTRATION_STYLE,
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'maximum_concentration_{year}'],
        ),
        # TODO: Extract to helper
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
                args=['foo'],
            ),
        ],
    )


layers = [_layer(year) for year in CONCENTRATION_YEARS]
