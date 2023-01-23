import json
from typing import Literal

from qgreenland.config.datasets.seaice import seaice_age as dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.constants.paths import CONFIG_DIR
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

PARAMS_FP = CONFIG_DIR / "helpers/ancillary/sea_ice_age_params.json"


def _get_layer_params():
    with open(PARAMS_FP, "r") as f:
        return json.loads(f.read())


seaice_age_layers = _get_layer_params()

AgeType = Literal["minimum", "maximum"]


def sea_ice_age_layer(year: int, age_type: AgeType) -> Layer:
    layer_info = seaice_age_layers[year][age_type]

    return Layer(
        id=f"seaice_{age_type}_age_{year}",
        title=f"{layer_info['date_range']} {year}",
        description=(
            f"""Age of sea ice derived from weekly averaged ice motion vectors. A
            value of N indicates ice aged N-1 to N years. A value of 20 represents
            land; 21 represents ocean cells where ice age was not calculated. Week
            of {age_type} extent chosen based on NSDIC's Sea Ice Index 5-day
            average."""
        ),
        tags=[],
        style="sea_ice_age",
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[str(year)],
        ),
        steps=[
            CommandStep(
                args=[
                    "gdal_translate",
                    # Override the source SRS, which is not recognized by gdal
                    # >=3.5.0. Previous versions of gdal identified the
                    # coordinate system but did so incorrectly. Instead of
                    # identifying the CRS as the legacy EASE projection
                    # (EPSG:3408) it identifies it as EASE2 (EPSG:6091). This is
                    # because EPSG:3408 is deprecated in favor of
                    # EPSG:6091. This association is NOT correct - they each
                    # have different datums and should not be treated as
                    # interchangeable.
                    "-a_srs",
                    (
                        '"+proj=laea +lat_0=90 +lon_0=0 +x_0=0'
                        ' +y_0=0 +a=6371228 +b=6371228 +units=m +no_defs"'
                    ),
                    "-b",
                    layer_info["band_num"],
                    (
                        "NETCDF:{input_dir}/"
                        f"iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc:age_of_sea_ice"
                    ),
                    "{output_dir}/age_of_sea_ice.tif",
                ],
            ),
            *gdal_edit(
                input_file="{input_dir}/age_of_sea_ice.tif",
                output_file="{output_dir}/edited.tif",
                gdal_edit_args=[
                    "-a_ullr",
                    "-4518421 4518421 4506579 -4506579",
                ],
            ),
            *warp_and_cut(
                input_file="{input_dir}/edited.tif",
                output_file="{output_dir}/warped_and_cut.tif",
                cut_file=project.boundaries["background"].filepath,
                reproject_args=[
                    "-tr",
                    "12500",
                    "12500",
                ],
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/warped_and_cut.tif",
                output_file="{output_dir}/overviews.tif",
                dtype_is_float=False,
            ),
        ],
    )


def create_sea_ice_age_layers(age_type: AgeType) -> list[Layer]:
    return [sea_ice_age_layer(year, age_type) for year in seaice_age_layers.keys()]
