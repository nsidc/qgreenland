from qgreenland.config.datasets.arctic_vegetation_biomass import (
    arctic_vegetation_biomass_2010 as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

vegetation_biomass_2010 = Layer(
    id="vegetation_biomass_2010",
    title="Vegetation biomass 2010 (12.4km)",
    description=(
        """Estimated above ground plant biomass for the tundra biome in
        kilograms per square meter. Based on trans-Arctic field data and AVHRR
        NDVI. Data provided by ORNL DAAC."""
    ),
    tags=[],
    style="vegetation_biomass",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *warp(
            input_file="{input_dir}/aga_circumpolar_avhrr_biomass_2010.tif",
            output_file="{output_dir}/warped.tif",
            cut_file=project.boundaries["data"].filepath,
            warp_args=(
                "-tr",
                "12400",
                "12400",
            ),
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/warped.tif",
            output_file="{output_dir}/compressed.tif",
            dtype_is_float=True,
        ),
    ],
)
