from typing import Literal

from qgreenland.config.datasets.seaice import seaice_age as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: calculate band_num dynamically. Ideally we pull the date of the minimum
# for each year from the sea ice index, and then find the band that has a date
# range that intersects that minimum? This would only be possible post fetch and
# would probably require some additional python code to open the fetched granule
# and get the date range associated with each band.
seaice_age_layers = {
    2010: {
        'minimum': {
            'date_range': 'September 17-24',
            'band_num': 38,  # Week of 2010-09-17
        },
        'maximum': {
            'date_range': 'March 26-April 2',
            'band_num': 13,  # Week of 2010-03-26
        },
    },
    2011: {
        'minimum': {
            'date_range': 'September 10-17',
            'band_num': 37,  # Week of 2011-09-10
        },
        'maximum': {
            'date_range': 'March 5-12',
            'band_num': 10,  # Week of 2011-03-05
        },
    },
    2012: {
        'minimum': {
            'date_range': 'September 16-23',
            'band_num': 38,  # Week of 2012-09-16
        },
        'maximum': {
            'date_range': 'March 18-25',
            'band_num': 12,  # Week of 2012-03-18
        },
    },
    2013: {
        'minimum': {
            'date_range': 'September 10-17',
            'band_num': 38,  # Week of 2013-09-10
        },
        'maximum': {
            'date_range': 'March 12-19',
            'band_num': 11,  # Week of 2013-03-12
        },
    },
    2014: {
        'minimum': {
            'date_range': 'September 17-24',
            'band_num': 38,  # Week of 2014-09-17
        },
        'maximum': {
            'date_range': 'March 19-26',
            'band_num': 12,  # Week of 2014-03-19
        },
    },
    2015: {
        'minimum': {
            'date_range': 'September 3-10',
            'band_num': 36,  # Week of 2015-09-03
        },
        'maximum': {
            'date_range': 'February 12-19',
            'band_num': 7,  # Week of 2015-02-12
        },
    },
    2016: {
        'minimum': {
            'date_range': 'September 9-16',
            'band_num': 37,  # Week of 2016-09-09
        },
        'maximum': {
            'date_range': 'March 18-25',
            'band_num': 12,  # Week of 2016-03-18
        },
    },
    2017: {
        'minimum': {
            'date_range': 'September 10-17',
            'band_num': 37,  # Week of 2017-09-10
        },
        'maximum': {
            'date_range': 'March 5-12',
            'band_num': 10,  # Week of 2017-03-05
        },
    },
    2018: {
        'minimum': {
            'date_range': 'September 17-24',
            'band_num': 38,  # Week of 2018-09-17
        },
        'maximum': {
            'date_range': 'March 11-18',
            'band_num': 10,  # Week of 2018-03-12
        },
    },
    2019: {
        'minimum': {
            'date_range': 'September 17-24',
            'band_num': 38,  # Week of 2019-09-17
        },
        'maximum': {
            'date_range': 'March 12-19',
            'band_num': 11,  # Week of 2019-03-12
        },
    },
    # TODO: 2020 data is now available!
}


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
