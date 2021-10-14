from qgreenland.config.datasets.asiaq_placenames import asiaq_private_placenames
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput

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
        *ogr2ogr(
            input_file='{input_dir}/translations_joined.gpkg',
            output_file='{output_dir}/final.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-sql', (
                    "'SELECT *, \"New Greenlandic\" as label"
                    ' FROM translations_joined'
                    " WHERE \"Object designation\" IN (\"BY\", \"BYGD\")'"
                ),
            ),
        ),
    ],
)

comprehensive_places = towns_and_settlements.copy(update={
    'id': 'comprehensive_places',
    'title': 'Place names database',
    'description': 'Points representing named points of interest in Greenland.',
    'steps': [
        *ogr2ogr(
            input_file='{input_dir}/translations_joined.gpkg',
            output_file='{output_dir}/final.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-sql', (
                    "'SELECT *, \"English explanation of Object designation\""
                    ' || ":" || "New Greenlandic" as label'
                    " FROM translations_joined'"
                ),
            ),
        ),
    ],
})
