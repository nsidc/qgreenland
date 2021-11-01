from qgreenland.config.datasets.nafo_divisions import nafo_divisions as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


nafo_divisions = ConfigLayer(
    id='nafo_divisions',
    title='NAFO divisions',
    description=(
        """The Northwest Atlantic Fisheries Organization zones."""
    ),
    tags=[],
    style='nafo_divisions',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/Divisions.zip',
            output_file='{output_dir}/final.gpkg',
            vector_filename='Divisions/*.shp',
        ),
    ],
)
