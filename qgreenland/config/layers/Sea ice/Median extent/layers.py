from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.seaice import layer_id, layer_title
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer, LayerInput


def _asset(dataset: Dataset, month: int) -> HttpAsset:
    asset = dataset.assets[f'median_extent_line_{month:02d}']
    if type(asset) is HttpAsset:
        return asset
    else:
        raise RuntimeError(f'Expected HTTP asset. Received: {asset}')


layers = [
    Layer(
        id=layer_id(month),
        title=layer_title(month),
        description=(
            """Ice edge position line that is typical for a month, based on median
            extent from the period 1981 through 2010."""
        ),
        tags=[],
        input=LayerInput(
            dataset=dataset,
            asset=_asset(dataset, month),
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/' + _asset(dataset, month).urls[0].split('/')[-1],
                output_file='{output_dir}/final.gpkg',
            ),
        ],
    ) for month in range(1, 12 + 1)
]
