from qgreenland.config.datasets.basal_thermal_state import (
    basal_thermal_state as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

basal_thermal_state = Layer(
    id="basal_thermal_state",
    title="Likely basal thermal state June 23 1993 - April 26 2013 (5km)",
    description=("""Likely basal frozen/thawed state of the Greenland Ice Sheet."""),
    tags=[],
    style="basal_thermal_state",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        CommandStep(
            args=[
                "gdalmdimtranslate",
                "-array",
                "name=likely_basal_thermal_state,transpose=[1,0],view=[::-1,:]",
                "{input_dir}/RDBTS4_Greenland_1993_2013_01_basal_thermal_state.nc",
                "{output_dir}/basal_thermal_state.tif",
            ],
        ),
        # Convert the dataset to `Int16` data type to save a little extra space
        # in the final output.
        CommandStep(
            args=[
                "gdal_calc.py",
                "--type",
                "Int16",
                # Set a nodata value of 3. This value does not occur in the data
                # (valid values are -1, 0, 1).
                "--NoDataValue",
                "3",
                # This dataset contains nans. Replace them with the nodata value (3)
                '--calc="nan_to_num(A, nan=3)"',
                "-A",
                "{input_dir}/basal_thermal_state.tif",
                "--outfile={output_dir}/basal_thermal_state.tif",
            ],
        ),
        *gdal_edit(
            input_file="{input_dir}/basal_thermal_state.tif",
            output_file="{output_dir}/basal_thermal_state.tif",
            gdal_edit_args=[
                "-a_ullr",
                "-632500.0 -667500.0 847500.0 -3342500.0",
                "-a_srs",
                "EPSG:3413",
            ],
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/basal_thermal_state.tif",
            output_file="{output_dir}/basal_thermal_state.tif",
            dtype_is_float=False,
        ),
    ],
)
