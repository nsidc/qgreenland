from qgreenland.config.datasets.geothermal_heat_flow import (
    geothermal_heat_flow as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

# The name of the `layer` variable doesn't matter here. You may create layers
# with a list comprehension as well, as long as you assign it to a variable.
geothermal_heat_flow = Layer(
    id="geothermal_heat_flow_map",
    title="Flow from multiple observations (55km)",
    style="geothermal_heat_flow_map",
    description=(
        """Geothermal heat flow map from machine-learning algorithm (55 km
        native resolution)."""
    ),
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["55km_map"],
    ),
    steps=[
        *warp_and_cut(
            input_file="{input_dir}/geothermal_heat_flow_map_55km.nc",
            output_file="{output_dir}/geothermal_heat_flow_map_55km.tif",
            cut_file=project.boundaries["data"].filepath,
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/geothermal_heat_flow_map_55km.tif",
            output_file="{output_dir}/geothermal_heat_flow_map_55km.tif",
            dtype_is_float=True,
        ),
    ],
)

geothermal_heat_flow_measurements = Layer(
    id="geothermal_heat_flow_measurements",
    title="Flow measurement locations",
    description=(
        """Heat flow measurement database used in the creation of the 'Flow from
        multiple observations (55km)' layer."""
    ),
    tags=[],
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["heat_flow_measurements"],
    ),
    steps=[
        *compressed_vector(
            input_file="{input_dir}/Greenland_heat_flow_measurements.zip",
            output_file="{output_dir}/heat_flow_measurements.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
        ),
    ],
)
