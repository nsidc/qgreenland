from qgreenland.config.datasets import bedmachine
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import Layer, LayerInput

bedmachine_fn = "BedMachineGreenland-v5.nc"


bed_datasets = {
    "thickness": {
        "title": "Ice thickness",
        "description": (
            """Ice thickness in meters. Mass conservation source data provided
            by Mathieu Morlighem."""
        ),
    },
    "surface": {
        "title": "Surface elevation",
        "description": (
            """Surface elevation in meters. Source is GIMP DEM v2.1
            (https://byrd.osu.edu/research/groups/glacier-dynamics/data/gimpdem)."""
        ),
    },
    "bed": {
        "title": "Bedrock elevation",
        "description": "Bedrock elevation in meters. Mass conservation source data provided by Mathieu Morlighem.",
    },
    "errbed": {
        "title": "Bed topography and ice thickness error",
        "description": (
            """Error estimate for Greenland bed elevation and ice thickness in
            meters."""
        ),
    },
}

layers = [
    Layer(
        id=f"bedmachine_{key}",
        title=f'{params["title"]} (150m)',
        description=params["description"],
        tags=["terrain_model"],
        style=f"bedmachine_{key}",
        input=LayerInput(
            dataset=bedmachine.bedmachine,
            asset=bedmachine.bedmachine.assets["only"],
        ),
        steps=[
            *warp_and_cut(
                input_file="NETCDF:{input_dir}/" + f"{bedmachine_fn}:{key}",
                output_file="{output_dir}/warped_and_cut.tif",
                cut_file="{assets_dir}/greenland_rectangle.geojson",
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/warped_and_cut.tif",
                output_file="{output_dir}/overviews.tif",
                dtype_is_float=False if key == "errbed" else True,
            ),
        ],
    )
    for key, params in bed_datasets.items()
]
