from qgreenland.config.datasets.land_ocean_shape import land_shape as dataset_land
from qgreenland.config.datasets.land_ocean_shape import ocean_shape as dataset_ocean
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput

land = ConfigLayer(
    id='land',
    title='land',
    description=(
        """Polygons representing the land."""
    ),
    tags=[],
    style='land',
    input=ConfigLayerInput(
        dataset=dataset_land,
        asset=dataset_land.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/ne_10m_land.zip',
            output_file='{output_dir}/final.gpkg',
        ),
    ],
)

ocean = ConfigLayer(
    id='ocean',
    title='ocean',
    description=(
        """Polygons representing the ocean."""
    ),
    tags=[],
    style='ocean',
    input=ConfigLayerInput(
        dataset=dataset_ocean,
        asset=dataset_ocean.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/ne_10m_ocean.zip',
            output_file='{output_dir}/final.gpkg',
        ),
    ],
)
