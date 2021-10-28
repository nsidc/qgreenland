from typing import Literal, cast

from qgreenland.config.datasets.lonlat import lonlat as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.asset import ConfigDatasetRepositoryAsset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


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
        in_package=True,
        style='lonlat',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=asset,
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/' + f'{asset.filepath.eval().name}',
                output_file='{output_dir}/' + f'{asset.filepath.eval().stem}.gpkg',
                boundary_filepath=project.boundaries['background'].filepath,
                ogr2ogr_args=[
                    '-segmentize',
                    f'{segment_max_distance}',
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
