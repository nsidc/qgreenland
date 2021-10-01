# TODO
from qgreenland.config.datasets.arctic_sea_routes import arctic_sea_routes as dataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


arctic_sea_routes = ConfigLayer(
    id='arctic_sea_routes',
    title='Arctic sea routes',
    description=(
        """Lines depict the Northern Sea Route, Northwest Passate, and
        hypothetical Transpolar Route."""
    ),
    tags=[],
    style='arctic_sea_routes',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO
    ],
)
