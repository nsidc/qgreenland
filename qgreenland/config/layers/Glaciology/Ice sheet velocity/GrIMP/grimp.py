from itertools import product

from qgreenland.config.datasets.grimp import grimp_annual_ice_velocity as annual_dataset
from qgreenland.config.datasets.grimp import (
    grimp_quarterly_ice_velocity as quarterly_dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


def make_layer(*, variable: str, layer_id: str, dataset, asset) -> Layer:
    return Layer(
        id=layer_id,
        # TODO: better title.
        title=layer_id,
        description="TODO.",
        # TODO:
        style=None,
        input=LayerInput(
            dataset=dataset,
            asset=asset,
        ),
        steps=[
            CommandStep(
                args=[
                    "gdal_calc.py",
                    "--calc",
                    '"round(A * 100.0)"',
                    "--NoDataValue",
                    "-9999",
                    "--type",
                    "Int32",
                    "-A",
                    "{input_dir}/" + f"*{variable}*.tif",
                    "--outfile",
                    "{output_dir}/scaled.tif",
                ],
            ),
            *gdal_edit(
                input_file="{input_dir}/scaled.tif",
                output_file="{output_dir}/edited.tif",
                gdal_edit_args=[
                    "-scale",
                    "0.01",
                ],
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/edited.tif",
                output_file="{output_dir}/compressed_with_overviews.tif",
                dtype_is_float=False,
            ),
        ],
    )


_start_year = 2021
_end_year = 2021
_variables = ("vv", "vx", "vy")

annual_grimp_layers = [
    make_layer(
        variable=variable,
        layer_id=f"grimp_annual_{variable}_{year}",
        dataset=annual_dataset,
        asset=annual_dataset.assets[str(year)],
    )
    for year, variable in product(range(_start_year, _end_year + 1), _variables)
]

quarterly_grimp_layers = [
    make_layer(
        variable=variable,
        layer_id=f"grimp_quarterly_{asset_id}_{variable}",
        dataset=quarterly_dataset,
        asset=quarterly_dataset.assets[asset_id],
    )
    for asset_id, variable in product(quarterly_dataset.assets.keys(), _variables)
]
