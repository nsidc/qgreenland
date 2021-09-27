import calendar

from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


def _asset(dataset: ConfigDataset, month: int) -> ConfigDatasetHttpAsset:
    return dataset.assets[f'median_extent_line_{month:02d}']


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
            *zipped_vector(
                input_file='{input_dir}/' + _asset(dataset, month).urls[0].split('/')[-1],
                output_file='{output_dir}/final.gpkg',
            ),
        ],
    ) for month in range(1, 12+1)
]
