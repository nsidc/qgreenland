from itertools import product

from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


def depth_str(depth: int) -> str:
    if depth == 0:
        return "Surface"
    else:
        return f"{depth}m"


def id_str(*, depth: int, season: str, variable: str) -> str:
    return f"woa_{depth}m_{variable}_{season}"


SEASONS = ("winter", "summer")

# Looks like these are the same for salinity.
DEPTHS_BANDS: dict[int, int] = {
    0: 1,
    50: 11,
    200: 25,
    500: 37,
}

# Sort by season first, then by depth
TEMPERATURE_COMBINATIONS = list(product(SEASONS, DEPTHS_BANDS.keys()))
TEMPERATURE_COMBINATIONS.sort(key=lambda x: x[0], reverse=True)
TEMPERATURE_COMBINATIONS.sort(key=lambda x: x[1])

SALINITY_COMBINATIONS = list(product(SEASONS, DEPTHS_BANDS.keys()))
SALINITY_COMBINATIONS.sort(key=lambda x: x[0], reverse=True)
SALINITY_COMBINATIONS.sort(key=lambda x: x[1])

WOA_TEMPERATURE_LAYER_ORDER = [
    id_str(depth=depth, season=season, variable="temperature")
    for (season, depth) in TEMPERATURE_COMBINATIONS
]
WOA_SALINITY_LAYER_ORDER = [
    id_str(depth=depth, season=season, variable="salinity")
    for (season, depth) in SALINITY_COMBINATIONS
]


def get_fn(*, season, variable):
    season_num = {
        "winter": 13,
        "summer": 15,
    }
    return f"woa23_decav91C0_{variable[0]}{season_num[season]}_04.nc"


def make_layer(*, dataset, depth, season, variable, units) -> Layer:
    return Layer(
        id=id_str(depth=depth, season=season, variable=variable),
        title=f"{depth_str(depth)}, {season.title()}",
        description=(
            f"""Average seawater {variable} at {depth_str(depth).lower()} depth
            in {units} for the 1991 - 2020 climate normal period.

            Climate normals, defined as 30-year averages of data by the World
            Meteorological Organization (WMO), provide long-term means for
            initializing models, environmental studies, checking in situ
            observations, etc.

            Comparing new observations to the most recent climate normal allows
            one to assess whether or not current observations are within the
            statistical norm in the context of the most recent 30-year
            climatological background. Additional applications, such as
            initializing boundary conditions for climate models or assessing
            remotely sensed observations, also require a more recent
            climatology."""
        ),
        packaging_tags=["core"],
        style=f"seawater_{variable}",
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[f"seasonal_{season}"],
        ),
        steps=[
            CommandStep(
                args=[
                    "gdal_translate",
                    "-b",
                    DEPTHS_BANDS[depth],
                    "NETCDF:{input_dir}/"
                    + get_fn(season=season, variable=variable)
                    + f":{variable[0]}_an",
                    "{output_dir}/extracted.tif",
                ],
            ),
            *warp_and_cut(
                input_file="{input_dir}/extracted.tif",
                output_file="{output_dir}/warped_and_cut.tif",
                cut_file=project.boundaries["background"].filepath,
                reproject_args=(
                    "-tr",
                    "25000",
                    "25000",
                    # A "target extent" bounding box is required to reproject
                    # this correctly, or we receive an error like:
                    #     ERROR 1: Attempt to create 0x1 dataset is
                    #     illegal,sizes must be larger than zero.
                    "-te",
                    *(
                        project.boundaries["background"].bbox.min_x,
                        project.boundaries["background"].bbox.min_y,
                        project.boundaries["background"].bbox.max_x,
                        project.boundaries["background"].bbox.max_y,
                    ),
                ),
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/warped_and_cut.tif",
                output_file="{output_dir}/final.tif",
                dtype_is_float=True,
            ),
        ],
    )
