from qgreenland.config.datasets.racmo import racmo_qgreenland_jan2021 as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
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
        ),
    ],
)
