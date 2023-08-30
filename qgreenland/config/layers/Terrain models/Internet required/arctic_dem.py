from qgreenland.config.datasets.arctic_dem import arctic_dem_online_v4_1 as dataset
from qgreenland.models.config.layer import Layer, LayerInput

arctic_dem_online = Layer(
    id="arctic_dem",
    title="Arctic DEM",
    description="Surface elevation in meters.",
    in_package=True,
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
)
