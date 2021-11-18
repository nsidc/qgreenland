import qgreenland.config.datasets.political_boundaries as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput


nunagis_municipalities_population = Layer(
    id='nunagis_municipalities_population',
    title='Greenland municipalities and population 2019',
    description=(
        """Polygons representing municipalities of Greenland and associated
        population numbers for 2019."""
    ),
    tags=[],
    style='nunagis_municipalities_population',
    input=LayerInput(
        dataset=dataset.nunagis_pop2019_municipalities,
        asset=dataset.nunagis_pop2019_municipalities.assets['only'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/fetched.geojson',
            output_file='{output_dir}/nunagis_municipalities_population.gpkg',
        ),
    ],
)

ne_states_provinces = Layer(
    id='ne_states_provinces',
    title='Global administrative divisions',
    description=(
        """Polygons representing countries' internal administrative
        boundaries."""
    ),
    tags=[],
    style='administrative_divisions',
    input=LayerInput(
        dataset=dataset.ne_states_provinces,
        asset=dataset.ne_states_provinces.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/ne_10m_admin_1_states_provinces.zip',
            output_file='{output_dir}/ne_states_provinces.gpkg',
        ),
    ],
)

ne_countries = Layer(
    id='ne_countries',
    title='Countries',
    description=(
        """Polygons representing countries."""
    ),
    tags=[],
    style='countries',
    input=LayerInput(
        dataset=dataset.ne_countries,
        asset=dataset.ne_countries.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/ne_10m_admin_0_countries.zip',
            output_file='{output_dir}/ne_countries.gpkg',
        ),
    ],
)
