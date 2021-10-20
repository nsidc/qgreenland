from qgreenland.config.datasets.geothermal_heat_flux import (
    geothermal_heat_flux as dataset,
)
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


extract_fp = (
    'ADS/ArCS-T2/A20180227-001/v200/dataset/'
    'GHF_Greenland_Ver2.0_GridEPSG3413_05km.nc'
)
nc_dataset = 'GHF'

geothermal_heat_flux = ConfigLayer(
    id='geothermal_heat_flux',
    title='Geothermal heat flux (5km)',
    description=(
        """Geothermal heat flux interpolated from ice core measurements in
        miliwatts per square meter."""
    ),
    tags=[],
    style='geothermal_heat_flux',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/A20180227-001v200.zip',
            decompress_contents_mask=extract_fp,
        ),
        *warp(
            input_file='NETCDF:{input_dir}/' + f'{extract_fp}:{nc_dataset}',
            output_file='{output_dir}/warped.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/warped.tif',
            output_file='{output_dir}/final.tif',
        ),
    ],
)
