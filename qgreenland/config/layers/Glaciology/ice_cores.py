from qgreenland.config.datasets.ice_cores import ice_cores as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ice_cores = ConfigLayer(
    id='ice_cores',
    title='Ice cores',
    description=(
        """Point locations of ice cores sampled in Greenland."""
    ),
    tags=[],
    style='labeled_point',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/paleo_icecore.kmz',
            output_file='{output_dir}/final.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-sql', (
                    """'SELECT *, Name as label
                    FROM "Ice Core"'"""
                ),
            ),
        ),
    ],
)
