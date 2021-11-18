from typing import Literal, cast

from qgreenland.config.datasets.lonlat import lonlat as dataset
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.config.project import project
from qgreenland.models.config.asset import ConfigDatasetRepositoryAsset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _make_lonlat_layer(
    asset: ConfigDatasetRepositoryAsset,
) -> ConfigLayer:
    deg_str = asset.id.rsplit('_', maxsplit=1)[0].split('_', maxsplit=1)[1]
    deg = deg_str.replace('_', '.')

    if asset.id.startswith('lat'):
        title_prefix = 'Latitude'
        segment_max_distance = 1
    elif asset.id.startswith('lon'):
        title_prefix = 'Longitude'
        segment_max_distance = 100
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
        tags=['reference'],
        style='lonlat',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=asset,
        ),
        # Separate steps to avoid incorrecrly clipping lattitude lines
        steps=[
            # Clip the datast
            ConfigLayerCommandStep(
                args=[
                    'ogr2ogr',
                    - 't_srs EPSG:3413' \
                    - 'where "wgs84Decimal >= 40"' \
                    '{output_dir}/clipped.gpkg',
                    '{input_dir}/*.geojson',
                ],
            ),
        ],
    )


def make_lonlat_layers(
    asset_prefix: Literal['lon', 'lat'],
) -> list[ConfigLayer]:
    assets = [
        cast(ConfigDatasetRepositoryAsset, asset)
        for asset in dataset.assets.values()
        if asset.id.startswith(asset_prefix)
    ]

    return [_make_lonlat_layer(asset) for asset in assets]
