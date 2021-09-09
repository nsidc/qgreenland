from typing import Literal, cast

from qgreenland.config.constants import PROJECT_CRS
from qgreenland.config.datasets.lonlat import lonlat as dataset
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
        in_package=True,
        style='lonlat',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=asset,
        ),
        steps=[
            # TODO: Extract as ogr2ogr segmentize helper?
            ConfigLayerCommandStep(
                args=[
                    'ogr2ogr',
                    '-lco',
                    'ENCODING=UTF-8',
                    '-t_srs',
                    f'{PROJECT_CRS}',
                    '-clipdst',
                    '{assets_dir}/latitude_shape_40_degrees.geojson',
                    '-segmentize',
                    f'{segment_max_distance}',
                    '{output_dir}/' + f'{asset.filepath.stem}.gpkg',
                    '{input_dir}/' + f'{asset.filepath.name}',
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
