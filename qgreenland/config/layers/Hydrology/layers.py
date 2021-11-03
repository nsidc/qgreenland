from qgreenland.config.datasets.esa_cci import esa_cci_marginal_lakes
from qgreenland.config.helpers.layers.streams_outlets_basins import layers  # noqa: F401
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


marginal_lakes = ConfigLayer(
    id='marginal_lakes',
    title='Inventory of ice marginal lakes, 2017',
    description=(
        """Polygons representing marginal lake locations identified from remote
        sensing."""
    ),
    tags=[],
    style=None,
    input=ConfigLayerInput(
        dataset=esa_cci_marginal_lakes,
        asset=esa_cci_marginal_lakes.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/20170101-ESACCI-L3S_GLACIERS-IML-MERGED-fv1.zip',
            output_file='{output_dir}/marginal_lakes.gpkg',
        ),
    ],
)
