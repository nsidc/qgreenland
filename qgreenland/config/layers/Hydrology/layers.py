from qgreenland.config.datasets.streams_outlets_basins import streams_outlets_basins as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ice_outlets = ConfigLayer(
    id='ice_outlets',
    title='Ice outlets',
    description=(
        """Calculated locations for subglacial hydrologic basin
        ice-margin-terminating outlets."""
    ),
    tags=[],
    style='ice_outlets',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['ice_outlets'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/outlets.gpkg',
            output_file='{output_dir}/ice_outlets.gpkg',
        ),
    ],
)
