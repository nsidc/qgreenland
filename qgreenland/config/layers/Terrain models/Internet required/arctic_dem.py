from qgreenland.config.datasets.arctic_dem import arctic_dem_online_v4_1 as dataset
from qgreenland.models.config.layer import Layer, LayerInput

arctic_dem_online = Layer(
    id="arctic_dem",
    title="Arctic DEM",
    description=(
        """Surface elevation in meters.

Note that the Polar Geospatial Center also provides custom download options for
a 32m ArcticDEM for QGreenland users. Learn about these add-on data for
QGreenland here:
https://qgreenland.readthedocs.io/en/latest/user/reference/addons/arctic-dem-addon-data.html
"""
    ),
    in_package=True,
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
)
