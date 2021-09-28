from qgreenland.config.datasets.seaice import seaice_age as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: this is weekly data, so does it relaly belong in a group called
# 'September'?


# TODO: calculate band_num dynamically. Ideally we pull the date of the minimum
# for each year from the sea ice index, and then find the band that has a date
# range that intersects that minimum? This would only be possible post fetch and
# would probably require some additional python code to open the fetched granule
# and get the date range associated with each band.
seaice_minimums = {
    2010: {
        'date_range': 'September 17-24',
        'band_num': 38,  # Week of 2010-09-17
    },
    2011: {
        'date_range': 'September 10-17',
        'band_num': 37,  # Week of 2011-09-10
    },
    2012: {
        'date_range': 'September 16-23',
        'band_num': 38,  # Week of 2012-09-16
    },
    2013: {
        'date_range': 'September 10-17',
        'band_num': 38,  # Week of 2013-09-10
    },
    2014: {
        'date_range': 'September 17-24',
        'band_num': 38,  # Week of 2014-09-17
    },
    2015: {
        'date_range': 'September 3-10',
        'band_num': 36,  # Week of 2015-09-03
    },
    2016: {
        'date_range': 'September 9-16',
        'band_num': 37,  # Week of 2016-09-09
    },
    2017: {
        'date_range': 'September 10-17',
        'band_num': 37,  # Week of 2017-09-10
    },
    2018: {
        'date_range': 'September 17-24',
        'band_num': 38,  # Week of 2018-09-17
    },
    2019: {
        'date_range': 'September 17-24',
        'band_num': 38,  # Week of 2019-09-17
    },
    # TODO: 2020 data is now available!
}


def _layer(year: int) -> ConfigLayer:
    layer_info = seaice_minimums[year]

    return ConfigLayer(
        id=f'seaice_minimum_age_{year}',
        title=f"{layer_info['date_range']} {year}",
        description=(
            """Age of sea ice derived from weekly averaged ice motion vectors. A
            value of N indicates ice aged N-1 to N years. A value of 20 represents
            land; 21 represents ocean cells where ice age was not calculated. Week
            of minimum extent chosen based on NSDIC's Sea Ice Index 5-day
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
                    'NETCDF:{input_dir}/' + f'iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc:age_of_sea_ice',
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


seaice_minimum_age_layers = [
    _layer(year) for year in seaice_minimums.keys()
]
