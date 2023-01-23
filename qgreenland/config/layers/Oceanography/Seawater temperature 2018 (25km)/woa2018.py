from qgreenland.config.datasets.woa2018_temperature import (
    woa2018_temperature as dataset,
)
from qgreenland.config.helpers.layers.woa2018 import (
    COMBINATIONS,
    DEPTHS_BANDS,
    SEASONS_FNS,
    depth_str,
    id_str,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

layers = [
    Layer(
        id=id_str(depth=depth, season=season),
        title=f"{depth_str(depth)}, {season.title()}",
        description=(
            f"Seawater temperature at {depth_str(depth).lower()} depth in °C."
        ),
        tags=[],
        style="seawater_temperature",
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
                    "NETCDF:{input_dir}/" + f"{SEASONS_FNS[season]}:t_an",
                    "{output_dir}/extracted.tif",
                ],
            ),
            *warp_and_cut(
                input_file="{input_dir}/extracted.tif",
                output_file="{output_dir}/warped_and_cut.tif",
                cut_file=project.boundaries["data"].filepath,
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
                        project.boundaries["data"].bbox.min_x,
                        project.boundaries["data"].bbox.min_y,
                        project.boundaries["data"].bbox.max_x,
                        project.boundaries["data"].bbox.max_y,
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
    for season, depth in COMBINATIONS
]
