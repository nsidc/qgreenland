from qgreenland.config.datasets.gravity_anomalies import gravity_anomalies as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


bouguer_gravity_anomaly = ConfigLayer(
    id='bouguer_gravity_anomaly',
    title='Bouguer gravity anomaly (2km)',
    description=(
        """Gravity anomalies in miligals (mGal)."""
    ),
    tags=[],
    style='gravity_anomaly',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/archive.zip',
            decompress_contents_mask='bouguer_gravity_anomaly.tif',
        ),
        *warp_and_cut(
            input_file='{input_dir}/bouguer_gravity_anomaly.tif',
            output_file='{output_dir}/bouguer_gravity_anomaly.tif',
            reproject_args=(
                # Source data is 0.02x-0.02 degrees resolution. Rene noted in
                # his email to QGreenland on 2021-01-22 that the geoid and
                # gravity anomaly grids are 2km resolution.
                '-tr', '2000', '2000',
            ),
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/bouguer_gravity_anomaly.tif',
            output_file='{output_dir}/bouguer_gravity_anomaly.tif',
        ),
    ],
)
