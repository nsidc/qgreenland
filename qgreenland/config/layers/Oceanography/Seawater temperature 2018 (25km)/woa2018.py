from itertools import product

from qgreenland.config.datasets.woa2018_temperature import (
    woa2018_temperature as dataset,
)
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


SEASONS_FNS: dict[str, str] = {
    'winter': 'woa18_decav_t13_04.nc',
    'summer': 'woa18_decav_t15_04.nc',
}
DEPTHS_BANDS: dict[int, int] = {
    0: 1,
    50: 11,
    200: 25,
    500: 37,
}
COMBINATIONS = product(SEASONS_FNS.keys(), DEPTHS_BANDS.keys())


def _depth_str(depth: int) -> str:
    if depth == 0:
        return 'surface'
    else:
        return f'{depth}m'


layers = [
    ConfigLayer(
        id=f'woa2018_{depth}m_temperature_{season}',
        title=f'{_depth_str(depth).title()}, {season.title()}',
        description=(
            f'Seawater temperature at {_depth_str(depth)} depth in °C.'
        ),
        tags=[],
        style='seawater_temperature',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'seasonal_{season}'],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'gdal_translate',
                    '-b', DEPTHS_BANDS[depth],
                    'NETCDF:{input_dir}/' + f'{SEASONS_FNS[season]}:t_an',
                    '{output_dir}/extracted.tif',
                ],
            ),
            *warp_and_cut(
                input_file='{input_dir}/extracted.tif',
                output_file='{output_dir}/warped_and_cut.tif',
                cut_file=project.boundaries['data'].filepath,
                reproject_args=(
                    '-tr', '25000', '25000',
                    # A "target extent" bounding box is required to reproject
                    # this correctly, or we receive an error like:
                    #     ERROR 1: Attempt to create 0x1 dataset is
                    #     illegal,sizes must be larger than zero.
                    '-te', *(
                        project.boundaries['data'].bbox.min_x,
                        project.boundaries['data'].bbox.min_y,
                        project.boundaries['data'].bbox.max_x,
                        project.boundaries['data'].bbox.max_y,
                    ),
                ),
            ),
            *build_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/final.tif',
            ),
        ],
    ) for season, depth in COMBINATIONS
]
