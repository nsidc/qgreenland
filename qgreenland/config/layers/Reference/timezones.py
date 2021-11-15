from qgreenland.config.datasets.timezones import ne_timezones as dataset
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


timezones = Layer(
    id='timezones',
    title='Time zones',
    description=(
        """Polygons representing time zones."""
    ),
    tags=[],
    style='transparent_labeled_shape',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO: these steps the same as `compressed_vector` except with
        # `OGR_ENABLE_PARTIAL_REPROJECTION` envvar set for the `ogr2ogr`
        # step. DRY out?
        CommandStep(
            args=[
                'unzip',
                '{input_dir}/ne_10m_time_zones.zip',
                '-d', '{output_dir}',
            ],
        ),
        CommandStep(
            id='ogr2ogr',
            args=[
                'OGR_ENABLE_PARTIAL_REPROJECTION=True',
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '-clipdst', project.boundaries['background'].filepath,
                '-sql', (
                    """'SELECT *, name as label
                    FROM "ne_10m_time_zones"'"""
                ),
                '{output_dir}/reprojected_and_clipped.gpkg',
                '{input_dir}/*.shp',
            ],
        ),
    ],
)
