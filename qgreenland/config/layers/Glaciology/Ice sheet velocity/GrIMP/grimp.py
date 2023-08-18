from qgreenland.config.datasets.grimp import grimp_annual_ice_velocity as dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

grimp_vv_veloity_layers = [
    Layer(
        id=layer_id,
        # TODO: better title.
        title=layer_id,
        description="TODO.",
        # TODO:
        style=None,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[layer_id],
        ),
        steps=[
            *warp(
                input_file="{input_dir}/*vv*.tif",
                output_file="{output_dir}/downsampled.tif",
                cut_file=project.boundaries["data"].filepath,
                warp_args=[
                    "-tr",
                    "1500 1500",
                ],
            ),
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
                    "{input_dir}/downsampled.tif",
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
    for layer_id in [f"vv_{year}" for year in range(2015, 2021 + 1)]
]
