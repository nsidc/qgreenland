# TODO: `from qgreenland.helpers.? import ?` if needed
from qgreenland.config.datasets.gem_research_stations import (
    gem_research_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
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
        *ogr2ogr(
            input_file='{input_dir}/gem_research_stations.geojson',
            output_file='{output_dir}/final.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-sql', (
                    """'SELECT *, "Station Name" as label
                    FROM "gem_research_stations"'"""
                ),
            ),
        ),
    ],
)
