from qgreenland.config.datasets.ice_cores import ice_cores as dataset
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


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
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '-clipdst', project.boundaries['data'].filepath,
                '-makevalid',
                '-sql', (
                    """'SELECT *, Name as label
                    FROM "Ice Core"'"""
                ),
                '{output_dir}/final.gpkg',
                '{input_dir}/paleo_icecore.kmz',
            ],
        ),
    ],
)
