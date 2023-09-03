from typing import Literal

from qgreenland.config.datasets.esa_cci import (
    esa_cci_surface_elevation_change as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

_year_ranges = [
    (start_year, end_year)
    for start_year, end_year in zip(range(1992, 2016 + 1), range(1996, 2020 + 1))
]


SurfaceElevVar = Literal["SEC", "SECer"]


def surface_elevation_layer(
    *,
    array_index: int,
    start_year: int,
    end_year: int,
    variable: SurfaceElevVar,
) -> Layer:
    if variable == "SEC":
        description = """Rate of surface elevation change in meters per year.

               Data are based on ESAs Ku-band radar satellite level-2 data
               products."""
        style = "surface_elevation_change"
    else:
        description = """Error of rate of surface elevation change in meters per year.

            Data are based on ESAs Ku-band radar satellite level-2 data
            products."""
        style = "surface_elevation_change_errors"

    return Layer(
        id=f"surface_elevation_change_{variable.lower()}_{start_year}_{end_year}",
        title=f"Surface elevation change {start_year}-{end_year}",
        description=description,
        packaging_tags=["core"],
        style=style,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets["only"],
        ),
        steps=[
            decompress_step(
                input_file="{input_dir}/cci_sec_2021.zip",
            ),
            CommandStep(
                args=[
                    "gdalmdimtranslate",
                    "-co",
                    "COMPRESS=DEFLATE",
                    "-array",
                    f"name={variable},view=[:,:,{array_index}]",
                    "{input_dir}/Release/CCI_GrIS_RA_SEC_5km_Vers3.0_2021-08-09.nc",
                    "{output_dir}/" + f"{variable.lower()}_{start_year}_{end_year}.tif",
                ],
            ),
            *compress_and_add_overviews(
                input_file=(
                    "{input_dir}/" f"{variable.lower()}_{start_year}_{end_year}.tif"
                ),
                output_file="{output_dir}/overviews.tif",
                dtype_is_float=True,
            ),
        ],
    )


def surface_elevation_layers_for_var(*, variable: SurfaceElevVar):
    return [
        surface_elevation_layer(
            array_index=array_index,
            start_year=start_year,
            end_year=end_year,
            variable=variable,
        )
        for array_index, (start_year, end_year) in enumerate(_year_ranges)
    ]
