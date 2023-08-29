from typing import Literal, Union, cast

from qgreenland.config.datasets.lonlat import lonlat as dataset
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.config.project import project
from qgreenland.models.config.asset import RepositoryAsset
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep
from qgreenland.util.runtime_vars import EvalFilePath

lonlat_assets_sorted = sorted(
    dataset.assets.values(),
    key=lambda asset: float(".".join(asset.id.split("_")[1:-1])),
)
lonlat_ids_sorted = [a.id for a in lonlat_assets_sorted]


def _make_lonlat_layer(
    asset: RepositoryAsset,
) -> Layer:
    deg_str = asset.id.rsplit("_", maxsplit=1)[0].split("_", maxsplit=1)[1]
    deg = deg_str.replace("_", ".")

    ogr2ogr_clip_args: list[Union[str, EvalFilePath]]
    if asset.id.startswith("lat"):
        title_prefix = "Latitude"
        segment_max_distance = 1
        ogr2ogr_clip_args = [
            "-where",
            '"wgs84Decimal >= 40"',
        ]
    elif asset.id.startswith("lon"):
        title_prefix = "Longitude"
        segment_max_distance = 100
        ogr2ogr_clip_args = [
            "-clipdst",
            project.boundaries["background"].filepath,
        ]
    else:
        raise RuntimeError(
            "Expected asset ID starting with 'lon' or 'lat'; received:" f" {asset.id}",
        )

    return Layer(
        id=asset.id,
        title=f"{title_prefix} lines ({deg} degree)",
        description=(f"Lines of {title_prefix.lower()} in {deg}-degree resolution."),
        packaging_tags=["core"],
        style="lonlat",
        input=LayerInput(
            dataset=dataset,
            asset=asset,
        ),
        steps=[
            CommandStep(
                args=[
                    "ogr2ogr",
                    *STANDARD_OGR2OGR_ARGS,
                    "-segmentize",
                    segment_max_distance,
                    *ogr2ogr_clip_args,
                    "{output_dir}/clipped.gpkg",
                    "{input_dir}/*.geojson",
                ],
            ),
        ],
    )


def make_lonlat_layers(
    lon_or_lat: Literal["lon", "lat"],
) -> list[Layer]:
    assets = [
        cast(RepositoryAsset, asset)
        for asset in dataset.assets.values()
        if asset.id.startswith(lon_or_lat)
    ]

    return [_make_lonlat_layer(asset) for asset in assets]
