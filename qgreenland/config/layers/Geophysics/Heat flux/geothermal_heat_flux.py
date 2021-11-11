from qgreenland.config.datasets.geothermal_heat_flux import (
    geothermal_heat_flux as dataset,
)
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


nc_dataset = 'GHF'

geothermal_heat_flux = ConfigLayer(
    id='geothermal_heat_flux',
    title='Flux from ice cores (Greve, R.) (5km)',
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
        *warp(
            input_file='NETCDF:{input_dir}/' + f'GHF_Greenland_Ver2.0_GridEPSG3413_05km.nc:{nc_dataset}',
            output_file='{output_dir}/warped.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/warped.tif',
            output_file='{output_dir}/final.tif',
        ),
    ],
)
