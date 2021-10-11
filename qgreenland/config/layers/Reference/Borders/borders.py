from qgreenland.config.datasets.coastlines import bas_coastlines as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


bas_greenland_coastlines = ConfigLayer(
    id='bas_greenland_coastlines',
    title='Greenland coastlines 2017',
    description=(
        """This layer should be used as the 'reference coastline' for
        Greenland."""
    ),
    tags=[],
    style='greenland_coastline',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/Greenland_coast.zip',
            output_file='{output_dir}/greenland_coastline.gpkg',
        ),
    ],
)
