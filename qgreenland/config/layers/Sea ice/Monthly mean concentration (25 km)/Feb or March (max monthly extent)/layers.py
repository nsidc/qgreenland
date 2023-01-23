import calendar

from qgreenland.config.datasets.seaice import seaice_index as dataset
from qgreenland.config.helpers.layers.sea_ice_concentration import (
    CONCENTRATION_DESCRIPTION,
    CONCENTRATION_STYLE,
    MAX_CONCENTRATION_YEARS,
    conc_max_month,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


def _layer(year) -> Layer:
    month = conc_max_month(year)
    month_name = calendar.month_name[month]

    return Layer(
        id=f"seaice_maximum_concentration_{year}",
        title=f"{month_name} {year}",
        description=CONCENTRATION_DESCRIPTION,
        tags=[],
        style=CONCENTRATION_STYLE,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[f"maximum_concentration_{year}"],
        ),
        # TODO: Extract to helper
        steps=[
            CommandStep(
                args=[
                    "gdal_calc.py",
                    "--calc",
                    "'A / 10.0'",
                    "-A",
                    "{input_dir}/*.tif",
                    "--outfile={output_dir}/downscaled.tif",
                ],
            ),
            *warp_and_cut(
                input_file="{input_dir}/downscaled.tif",
                output_file="{output_dir}/warped_and_cut.tif",
                cut_file=project.boundaries["background"].filepath,
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/warped_and_cut.tif",
                output_file="{output_dir}/overviews.tif",
                dtype_is_float=False,
            ),
        ],
    )


layers = [_layer(year) for year in MAX_CONCENTRATION_YEARS]
