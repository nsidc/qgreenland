from qgreenland.config.datasets.basal_thermal_state import basal_thermal_state as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


basal_thermal_state = ConfigLayer(
    id='basal_thermal_state',
    title='Likely basal thermal state June 23 1993 - April 26 2013 (5km)',
    description=(
        """Likely basal frozen/thawed state of the Greenland Ice Sheet."""
    ),
    tags=[],
    style='basal_thermal_state',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'gdalmdimtranslate',
                '-array', 'name=likely_basal_thermal_state,transpose=[1,0],view=[::-1,:]',
                '{input_dir}/RDBTS4_Greenland_1993_2013_01_basal_thermal_state.nc',
                '{output_dir}/basal_thermal_state.tif',
            ],
        ),
        *gdal_edit(
            input_file='{input_dir}/basal_thermal_state.tif',
            output_file='{output_dir}/basal_thermal_state.tif',
            gdal_edit_args=[
                '-a_ullr', '-632500.0 -667500.0 847500.0 -3342500.0',
                '-a_srs', 'EPSG:3413',
                # Set a nodata value of 3. This value does not occur in the data
                # (valid values are -1, 0, 1). There _are_ `nan` values in this
                # data, and they show up in QGIS if nodata is unset. Setting
                # nodata to `nan` works, but causes the next step (building
                # overviews) to hang indefinitely.
                '-a_nodata', '3',
            ],
        ),
        *build_overviews(
            input_file='{input_dir}/basal_thermal_state.tif',
            output_file='{output_dir}/basal_thermal_state.tif',
            resampling_algorithm='nearest',
        ),
    ],
)
