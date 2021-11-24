from qgreenland.config.datasets.dms_gtk import (
    danish_agency_for_data_supply_and_efficiency_gtk_topo_map as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import compress_and_add_overviews
from qgreenland.models.config.layer import Layer, LayerInput


dms_gtk_topo = Layer(
    id='dms_gtk_topo',
    title='Topographic map (1 to 500,000)',
    description=(
        """Digitized and geolocated topographic map of Greenland."""
    ),
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # NOTE: This layer is not reprojected. We had some issues in the distant
        # past reprojecting this layer correctly. Its internal CRS is
        # `EPSG:32624`.
        *compress_and_add_overviews(
            input_file='{input_dir}/dms_gtk_topo.tif',
            output_file='{output_dir}/final.tif',
            dtype_is_float=False,
        ),
    ],
)
