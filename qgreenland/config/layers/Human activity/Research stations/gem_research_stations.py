# TODO: `from qgreenland.helpers.? import ?` if needed
from qgreenland.config.datasets.gem_research_stations import (
    gem_research_stations as dataset
)
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


gem_research_stations = ConfigLayer(
    id='gem_research_stations',
    title='GEM research stations',
    description=(
        """Location and description of Greenland Ecosystem Monitoring research
        stations."""
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
                    """'SELECT *, "Station Name" as label
                    FROM "gem_research_stations"'"""
                ),
                '{output_dir}/final.gpkg',
                '{input_dir}/gem_research_stations.geojson',
            ],
        ),

    ],
)
