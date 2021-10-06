from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.config.datasets.timezones import ne_timezones as dataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


timezones = ConfigLayer(
    id='timezones',
    title='Time zones',
    description=(
        """Polygons representing time zones."""
    ),
    tags=[],
    style='transparent_shape',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO: these steps the same as `zipped_vector` except with
        # `OGR_ENABLE_PARTIAL_REPROJECTION` envvar set for the `ogr2ogr`
        # step. DRY out?
        ConfigLayerCommandStep(
            args=[
                'unzip',
                '{input_dir}/ne_10m_time_zones.zip',
                '-d', '{output_dir}',
            ],
        ),
        ConfigLayerCommandStep(
            args=[
                'OGR_ENABLE_PARTIAL_REPROJECTION=True',
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '-clipdst', project.boundaries['background'].filepath,
                '{output_dir}/reprojected_and_clipped.gpkg',
                '{input_dir}/*.shp',
            ],
        ),
    ],
)
