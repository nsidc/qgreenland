import qgreenland.config.datasets.political_boundaries as dataset
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


nunagis_municipalities_population = ConfigLayer(
    id='nunagis_municipalities_population',
    title='Greenland municipalities and population 2019',
    description=(
        """Polygons representing municipalities of Greenland and associated
        population numbers for 2019."""
    ),
    tags=[],
    style='nunagis_municipalities_population',
    input=ConfigLayerInput(
        dataset=dataset.nunagis_pop2019_municipalities,
        asset=dataset.nunagis_pop2019_municipalities.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '{output_dir}/nunagis_municipalities_population.gpkg',
                '{input_dir}/fetched.geojson',
            ],
        ),
    ],
)
