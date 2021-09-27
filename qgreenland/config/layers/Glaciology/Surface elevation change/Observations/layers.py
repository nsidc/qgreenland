from qgreenland.config.datasets.esa_cci import esa_cci_surface_elevation_change as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


_year_ranges = [
    (start_year, end_year)
    for start_year, end_year
    in zip(range(1992, 2015 + 1), range(1996, 2019 + 1))
]


def surface_elevation_layer(
    *,
    array_index: int,
    start_year: int,
    end_year: int,
) -> ConfigLayer:
    return ConfigLayer(
        id=f'surface_elevation_change_{start_year}_{end_year}',
        title=f'Surface elevation change {start_year}-{end_year}',
        description=(
            """Rate of surface elevation change in meters per year."""
        ),
        tags=[],
        style='surface_elevation_change',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'gdalmdimtranslate',
                    '-array', f'name=SEC,view=[:,:,{array_index}]',
                    '{input_dir}/Release/CCI_GrIS_RA_SEC_5km_Vers2.0_2020-08-26.nc',
                    '{output_dir}/' + f'surf_elev_change_{start_year}_{end_year}.tif',
                ],
            ),
            *build_overviews(
                input_file='{input_dir}/' + f'surf_elev_change_{start_year}_{end_year}.tif',
                output_file='{output_dir}/overviews.tif',
            ),
        ],
    )


surface_elevation_change_layers = [
    surface_elevation_layer(
        array_index=array_index,
        start_year=start_year,
        end_year=end_year,
    )
    for array_index, (start_year, end_year) in enumerate(_year_ranges)
]
