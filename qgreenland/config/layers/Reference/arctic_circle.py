from qgreenland.config.datasets.arctic_circle import arctic_circle as dataset
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


arctic_circle = ConfigLayer(
    id='arctic_circle',
    title="Arctic Circle (66° 34' North)",
    description=(
        """The Arctic Circle is an imaginary line that circles the globe at
        approximately 66° 34' N and marks the latitude above which the sun does
        not set on the summer solstice, and does not rise on the winter
        solstice."""
    ),
    tags=[],
    style='arctic_circle',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                '-segmentize', '1',
                '-s_srs', 'EPSG:4326',
                '{output_dir}/arctic_circle.gpkg',
                '{input_dir}/arctic_circle.geojson',
            ],
        ),
    ],
)
