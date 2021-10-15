from qgreenland.config.datasets.ocean_shape import ocean_shape as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ocean = ConfigLayer(
    id='ocean',
    title='Ocean',
    description=(
        """Polygons representing the ocean."""
    ),
    tags=[],
    style='ocean',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/ne_10m_ocean.zip',
            output_file='{output_dir}/final.gpkg',
        ),
    ],
)
