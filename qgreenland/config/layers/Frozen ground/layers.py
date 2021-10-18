from qgreenland.config.datasets.pangaea_ground_temperature import pangaea_ground_temperature as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ground_temperature = ConfigLayer(
    id='ground_temperature',
    title='Ground temperature 2000-2016 (10km)',
    description=(
        """Average mean annual ground temperature in degrees Celsius."""
    ),
    tags=[],
    style='ground_temperature',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['10km'],
    ),
    steps=[
        *warp_and_cut(
            input_file='NETCDF:{input_dir}/UiO_PEX_5.0_20181127_2000_2016_10km.nc:MAGT',
            output_file='{output_dir}/ground_temperature.tif',
            reproject_args=[
                # Webpage for this data
                # (https://doi.pangaea.de/10.1594/PANGAEA.888600) notes All
                # files are provided in Arctic Polar Stereographic projection
                # (EPSG:3995 WGS 84)
                '-s_srs', 'EPSG:3995',
                '-tr', '10000', '10000',
            ],
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/ground_temperature.tif',
            output_file='{output_dir}/ground_temperature.tif',
        ),
    ],
)
