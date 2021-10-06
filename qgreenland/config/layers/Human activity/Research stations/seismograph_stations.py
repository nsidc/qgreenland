from qgreenland.config.datasets.seismograph_stations import (
    seismograph_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


seismograph_stations = ConfigLayer(
    id='seismograph_stations',
    title='Seismograph stations',
    description=(
        """Location and details of Greenland seismograph stations."""
    ),
    tags=[],
    style='seismograph_stations',
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
                '{output_dir}/ogr2ogr.gpkg',
                '{input_dir}/stations.kmz',
            ],
        ),
    ],
)
