from qgreenland.config.datasets.racmo import racmo_qgreenland_jan2021 as dataset
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


racmo_wind_vectors = ConfigLayer(
    id='racmo_wind_vectors',
    title='Annual mean wind vectors 1958-2019 (5km)',
    description=(
        """Averaged annual mean wind direction in meters per second from
        RACMO2.3p2 for the period 1958-2019."""
    ),
    tags=[],
    style='racmo_wind_vectors',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
            output_file='{output_dir}/racmo_wind_vectors.gpkg',
            vector_filename='wind_vector_points.gpkg',
            decompress_step_kwargs={
                'decompress_contents_mask': 'wind_vector_points.gpkg',
            },
        ),
    ],
)

racmo_wind_speed = ConfigLayer(
    id='racmo_wind_speed',
    title='Annual mean wind speed 1958-2019 (5km)',
    description=(
        """Averaged annual mean wind speed in meters per second from RACMO2.3p2
        for the period 1958-2019."""
    ),
    tags=[],
    style='racmo_wind_speed',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
            decompress_contents_mask='magnitudes.nc',
        ),
        *warp_and_cut(
            input_file='{input_dir}/magnitudes.nc',
            output_file='{output_dir}/racmo_wind_speed.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
    ],
)
