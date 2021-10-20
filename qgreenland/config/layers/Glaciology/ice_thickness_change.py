from qgreenland.config.datasets.ice_thickness_change import (
    icesheet_height_and_thickness_change as dataset,
)
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


SOURCE_FP = 'ICESat1_ICESat2_mass_change/gris.tif'

ice_thickness_change = ConfigLayer(
    id='ice_thickness_change',
    title='Ice column thickness rate of change 2003-2019 (5km)',
    description=(
        """Ice column thickness-change-rate estimates in meters per year based
        on data from NASA's ICESat and ICESat-2 satellites."""
    ),
    tags=[],
    style='ice_thickness_change',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/ICESat1_ICESat2_mass_change.zip',
            decompress_contents_mask=SOURCE_FP,
        ),
        *warp(
            input_file='{input_dir}/' + SOURCE_FP,
            output_file='{output_dir}/warped.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        *build_overviews(
            input_file='{input_dir}/warped.tif',
            output_file='{output_dir}/final.tif',
        ),
    ],
)
