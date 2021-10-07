from qgreenland.config.datasets.utm_zones import utm_zones as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


utm_zones = ConfigLayer(
    id='utm_zones',
    title='Universal Transverse Mercator (UTM) zones',
    description=(
        """Polygons representing Universal Transverse Mercator (UTM) zones."""
    ),
    tags=[],
    style='utm_zones',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            ogr2ogr_args=(
                '-where', '"\"ZONE\" != 0"',
            ),
            input_file='{input_dir}/utmzone.zip',
            output_file='{output_dir}/utm_zones.gpkg',
        ),
    ],
)
