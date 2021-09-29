import json
from typing import Literal

from qgreenland.config.datasets.seaice import seaice_age as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.constants import CONFIG_DIR
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _get_layer_params():
    params_fp = CONFIG_DIR / 'helpers/layers/sea_ice_age_params.json'
    with open(params_fp, 'r') as f:
        return json.loads(f.read())

    # TODO: check if list of years in layer params json file matches the list of
    # years identified by the dataset's assets. If not, run the (soon TM) code
    # to fetch assets and then re-run the code to generate the ice age params json.


seaice_age_layers = _get_layer_params()

AgeType = Literal['minimum', 'maximum']


def sea_ice_age_layer(year: int, age_type: AgeType) -> ConfigLayer:
    layer_info = seaice_age_layers[year][age_type]

    return ConfigLayer(
        id=f'seaice_{age_type}_age_{year}',
        title=f"{layer_info['date_range']} {year}",
        description=(
            f"""Age of sea ice derived from weekly averaged ice motion vectors. A
            value of N indicates ice aged N-1 to N years. A value of 20 represents
            land; 21 represents ocean cells where ice age was not calculated. Week
            of {age_type} extent chosen based on NSDIC's Sea Ice Index 5-day
            average."""
        ),
        tags=[],
        style='sea_ice_age',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[str(year)],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'gdal_translate',
                    '-b', layer_info['band_num'],
                    (
                        'NETCDF:{input_dir}/'
                        f'iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc:age_of_sea_ice'
                    ),
                    '{output_dir}/age_of_sea_ice.tif',
                ],
            ),
            ConfigLayerCommandStep(
                args=[
                    'cp', '{input_dir}/age_of_sea_ice.tif', '{output_dir}/edited.tif',
                    '&&',
                    'gdal_edit.py',
                    '-a_ullr', '-4518421 4518421 4506579 -4506579',
                    '{output_dir}/edited.tif',
                ],
            ),
            *warp_and_cut(
                input_file='{input_dir}/edited.tif',
                output_file='{output_dir}/warped_and_cut.tif',
                cut_file=project.boundaries['background'].filepath,
                reproject_args=(
                    '-tr', '12500', '12500',
                ),
            ),
            *build_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/overviews.tif',
            ),
        ],
    )


def create_sea_ice_age_layers(age_type: AgeType) -> list[ConfigLayer]:
    return [
        sea_ice_age_layer(year, age_type)
        for year in seaice_age_layers.keys()
    ]
