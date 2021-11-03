from qgreenland.config.datasets.geothermal_heat_flow import (
    geothermal_heat_flow as dataset,
)
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


# The name of the `layer` variable doesn't matter here. You may create layers
# with a list comprehension as well, as long as you assign it to a variable.
geothermal_heat_flow = ConfigLayer(
    id='geothermal_heat_flow_map',
    title='Geothermal heat flow (10km)',
    style='geothermal_heat_flow_map',
    description=(
        """Geothermal heat flow map from machine-learning algorithm (55 km
        native resolution)."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['55km_map'],
    ),
    steps=[
        *warp_and_cut(
            input_file='{input_dir}/geothermal_heat_flow_map_55km.nc',
            output_file='{output_dir}/geothermal_heat_flow_map_55km.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
    ],
)

geothermal_heat_flow_measurements = ConfigLayer(
    id='geothermal_heat_flow_measurements',
    title='Geothermal heat flow measurements',
    description=(
        """Heat flow measurement database used in the creation of the 'Geothermal
        heat flow map (10km)' layer."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['heat_flow_measurements'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/Greenland_heat_flow_measurements.zip',
            output_file='{output_dir}/heat_flow_measurements.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
        ),
    ],
)
