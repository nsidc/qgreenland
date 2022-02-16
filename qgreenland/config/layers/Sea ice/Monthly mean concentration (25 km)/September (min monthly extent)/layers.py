from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.sea_ice_concentration import (
    CONCENTRATION_DESCRIPTION,
    CONCENTRATION_STYLE,
    MIN_CONCENTRATION_YEARS,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import compress_and_add_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


layers = [
    Layer(
        id=f'seaice_minimum_concentration_{year}',
        title=f'September {year}',
        description=CONCENTRATION_DESCRIPTION,
        tags=[],
        style=CONCENTRATION_STYLE,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[f'minimum_concentration_{year}'],
        ),
        steps=[
            CommandStep(
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
            *compress_and_add_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/overviews.tif',
                dtype_is_float=False,
            ),
        ],
    ) for year in MIN_CONCENTRATION_YEARS
]
