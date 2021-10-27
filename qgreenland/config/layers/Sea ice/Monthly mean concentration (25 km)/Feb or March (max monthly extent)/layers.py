import calendar

from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.sea_ice_concentration import (
    CONCENTRATION_DESCRIPTION,
    CONCENTRATION_STYLE,
    CONCENTRATION_YEARS,
    conc_max_month,
)
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
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
            *warp_and_cut(
                input_file='{input_dir}/downscaled.tif',
                output_file='{output_dir}/warped_and_cut.tif',
                cut_file=project.boundaries['background'].filepath,
            ),
            *build_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/overviews.tif',
            ),
        ],
    )


layers = [_layer(year) for year in CONCENTRATION_YEARS]
