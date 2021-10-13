from qgreenland.config.datasets.arctic_vegetation_biomass import (
    arctic_vegetation_biomass_2010 as dataset,
)
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


vegetation_biomass_2010 = ConfigLayer(
    id='vegetation_biomass_2010',
    title='Vegetation biomass 2010 (12.4km)',
    description=(
        """Estimated above ground plant biomass for the tundra biome in
        kilograms per square meter. Based on trans-Arctic field data and AVHRR
        NDVI. Data provided by ORNL DAAC."""
    ),
    tags=[],
    style='vegetation_biomass',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *warp(
            input_file='{input_dir}/aga_circumpolar_avhrr_biomass_2010.tif',
            output_file='{output_dir}/warped.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
    ],
)
