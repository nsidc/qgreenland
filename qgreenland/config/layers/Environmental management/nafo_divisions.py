# TODO: Replace `XXXX` with the correct package/module/object to import
# TODO: `from qgreenland.config.project import project` if needed
from qgreenland.helpers.steps.zipped_vector import zipped_vector
from qgreenland.config.datasets.nafo_divisions import nafo_divisions as dataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
# TODO: Import the correct step type for steps populated below


nafo_divisions = ConfigLayer(
    id='nafo_divisions',
    title='NAFO divisions',
    description=(
        """The Northwest Atlantic Fisheries Organization zones"""
    ),
    tags=[],
    style='nafo_divisions',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/Divisions.zip'
            output_file='{output_dir}/final.gpkg',
        ),
    ],
)
