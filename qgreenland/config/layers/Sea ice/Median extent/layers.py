import calendar

from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


def _asset(dataset: ConfigDataset, month: int) -> ConfigDatasetHttpAsset:
    asset = dataset.assets[f'median_extent_line_{month:02d}']
    if type(asset) is ConfigDatasetHttpAsset:
        return asset
    else:
        raise RuntimeError(f'Expected HTTP asset. Received: {asset}')


layers = [
    ConfigLayer(
        id=f'seaice_median_extent_{month:02d}',
        title=calendar.month_name[month],
        description=(
            """Ice edge position line that is typical for a month, based on median
            extent from the period 1981 through 2010."""
        ),
        tags=[],
        input=ConfigLayerInput(
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
