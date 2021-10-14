from qgreenland.config.datasets.arctic_sea_routes import nga_arctic_sea_routes as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


arctic_sea_routes = ConfigLayer(
    id='arctic_sea_routes',
    title='Arctic sea routes',
    description=(
        """Lines depict the Northern Sea Route, Northwest Passate, and
        hypothetical Transpolar Route."""
    ),
    tags=[],
    style='arctic_sea_routes',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO: *compressed_vector(...)?
        ConfigLayerCommandStep(
            args=[
                'unzip',
                '-d', '{output_dir}',
                '{input_dir}/Shipping_and_Hydrography-shp.zip',
            ],
        ),
        *ogr2ogr(
            input_file='{input_dir}/Arctic_Sea_Routes.shp',
            output_file='{output_dir}/arctic_sea_routes.gpkg',
        ),
    ],
)
