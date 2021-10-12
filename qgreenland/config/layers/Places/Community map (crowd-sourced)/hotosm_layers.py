from qgreenland.config.datasets.hdx_hotosm import hdx_hotosm as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


hotosm_populated_places = ConfigLayer(
    id='hotosm_populated_places',
    title='Populated places',
    description=(
        """Points representing populated places in Greenland."""
    ),
    tags=[],
    style='hotosm_populated_places_point',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['populated_places'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/hotosm_grl_populated_places_points_shp.zip',
            output_file='{output_dir}/hotosm_populated_places.gpkg',
            ogr2ogr_args=(
                '-dialect', 'sqlite',
                '-sql', (
                    '"SELECT'
                    ' osm_id,'
                    ' is_in,'
                    ' source,'
                    ' name,'
                    ' place,'
                    ' geometry,'
                    ' CAST(population AS INTEGER) as population'
                    ' FROM hotosm_grl_populated_places_points"'
                ),
            ),
        ),
    ],
)
