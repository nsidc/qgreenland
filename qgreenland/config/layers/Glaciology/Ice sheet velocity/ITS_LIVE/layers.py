from qgreenland.config.datasets.velocity_mosaic import velocity_mosaic as dataset
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


velocity_mosaic = ConfigLayer(
    id='velocity_mosaic',
    title='Ice sheet velocity (120m)',
    description=(
        """Magnitude of velocity in meters per year."""
    ),
    tags=[],
    style='ice_sheet_velocity',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'gdal_calc.py',
                '--calc="A*B"',
                '--outfile={output_dir}/masked_velocity_mosaic.tif',
                '-A', 'NETCDF:{input_dir}/GRE_G0120_0000.nc:v',
                '-B', 'NETCDF:{input_dir}/GRE_G0120_0000.nc:ice',
            ],
        ),
        *warp_and_cut(
            input_file='{input_dir}/masked_velocity_mosaic.tif',
            output_file='{output_dir}/velocity_mosaic.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/velocity_mosaic.tif',
            output_file='{output_dir}/velocity_mosaic.tif',
        ),
    ],
)
