from qgreenland.config.datasets.asiaq_placenames import asiaq_private_placenames
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep

standard_ogr2ogr_args = [
    '-lco', 'ENCODING=UTF-8',
    '-t_srs', project.crs,
    # TODO: How to avoid this type of dir-handling within configs?
    '-clipdst', '{assets_dir}/' + str(project.boundaries['data'].filepath),
]

towns_and_settlements = ConfigLayer(
    id='populated_places',
    title='Towns and settlements',
    description='Points representing towns and settlements in Greenland.',
    tags=['places'],
    in_package=True,
    show=False,
    style='labeled_point',
    input=ConfigLayerInput(
        dataset=asiaq_private_placenames,
        asset=asiaq_private_placenames.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *standard_ogr2ogr_args,
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
                *standard_ogr2ogr_args,
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
