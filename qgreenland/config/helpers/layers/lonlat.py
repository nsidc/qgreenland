from typing import Literal

from qgreenland.config.datasets.lonlat import lonlat as dataset
from qgreenland.models.config.dataset import ConfigDatasetAsset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _make_lonlat_layer(
    asset: ConfigDatasetAsset,
) -> ConfigLayer:
    deg_str = asset.id.rsplit('_', maxsplit=1)[0].split('_', maxsplit=1)[1]
    deg = deg_str.replace('_', '.')

    if asset.id.startswith('lat'):
        title_prefix = 'Latitude'
    elif asset.id.startswith('lon'):
        title_prefix = 'Longitude'
    else:
        raise RuntimeError(
            "Expected asset ID starting with 'lon' or 'lat'; received:"
            f' {asset.id}',
        )

    return ConfigLayer(
        id=asset.id,
        title=f'{title_prefix} lines ({deg} degree)',
        description=(
            f'Lines of {title_prefix.lower()} in {deg}-degree resolution.'
        ),
        in_package=True,
        style='lonlat',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=asset,
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'ogr2ogr',

                ]

            ),
        ],
    )


def make_lonlat_layers(
    asset_prefix: Literal['lon', 'lat'],
) -> list[ConfigLayer]:
    assets = [
        asset for asset in dataset.assets.values()
        if asset.id.startswith(asset_prefix)
    ]

    return [_make_lonlat_layer(asset) for asset in assets]
