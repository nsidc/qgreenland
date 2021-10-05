from qgreenland.config.datasets.asiaq_placenames import asiaq_private_placenames
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep

towns_and_settlements = ConfigLayer(
    id='populated_places',
    title='Towns and settlements',
    description='Points representing towns and settlements in Greenland.',
    tags=['places'],
    style='labeled_point',
    input=ConfigLayerInput(
        dataset=asiaq_private_placenames,
        asset=asiaq_private_placenames.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                # TODO: How to convert this to an EvalStr? Should we allow args
                # to contain EvalPaths, EvalFilePaths, and EvalStrs?
                '-clipdst', project.boundaries['data'].filepath,
                '-makevalid',
                '-sql', (
                    "'SELECT *, \"New Greenlandic\" as label"
                    ' FROM translations_joined'
                    " WHERE \"Object designation\" IN (\"BY\", \"BYGD\")'"
                ),
                '{output_dir}/final.gpkg',
                '{input_dir}/translations_joined.gpkg',
            ],
        ),
    ],
)

comprehensive_places = towns_and_settlements.copy(update={
    'id': 'comprehensive_places',
    'title': 'Place names database',
    'description': 'Points representing named points of interest in Greenland.',
    'steps': [
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '-clipdst', project.boundaries['data'].filepath,
                '-makevalid',
                '-sql', (
                    "'SELECT *, \"English explanation of Object designation\""
                    ' || ":" || "New Greenlandic" as label'
                    " FROM translations_joined'"
                ),
                '{output_dir}/final.gpkg',
                '{input_dir}/translations_joined.gpkg',
            ],
        ),
    ],
})
