import qgreenland.config.datasets.political_boundaries as dataset
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
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

ne_states_provinces = ConfigLayer(
    id='ne_states_provinces',
    title='Global administrative divisions',
    description=(
        """Polygons representing countries' internal administrative
        boundaries."""
    ),
    tags=[],
    style='administrative_divisions',
    input=ConfigLayerInput(
        dataset=dataset.ne_states_provinces,
        asset=dataset.ne_states_provinces.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/ne_10m_admin_1_states_provinces.zip',
            output_file='{output_dir}/ne_states_provinces.gpkg',
        ),
    ],
)
