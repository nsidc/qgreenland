from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.step import ConfigLayerCommandStep

from scripts.experimental.pyconfig_spike.datasets.natural_earth import background as background_dataset
from scripts.experimental.pyconfig_spike.step_templates.warp_and_cut import warp_and_cut

background = ConfigLayer(
    id='background',
    title='Background (500m)',
    description='Stylized shaded-relief map for providing a general sense of geography.',
    hierarchy=['Basemaps'],
    in_package=True,
    show=True,
    input={
        'dataset': background_dataset,
        'asset': background_dataset.assets['high_res'],
    },
    steps=[
        ConfigLayerCommandStep(
            type='command',
            args=['unzip', '{input_dir}/*.zip', '-d', '{output_dir}'],
        ),
        *warp_and_cut(
            input_file='{input_dir}/NE2_HR_LC_SR_W/NE2_HR_LC_SR_W.tif',
            output_file='{output_dir}/warped_and_cut.tif',
            xRes=500,
            yRes=500,
            # TODO import project config and access correct boundary.
            target_extent='-5774572.727595 -5774572.727595 5774572.727595 5774572.727595',
            cut_file='{assets_dir}/latitude_shape_40_degrees.geojson',
        ),
    ],
)
