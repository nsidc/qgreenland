from qgreenland.config.datasets.natural_earth import background as background_dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


background = ConfigLayer(
    id='background',
    title='Background (500m)',
    description='Stylized shaded-relief map for providing a general sense of geography.',
    in_package=True,
    show=True,
    input=ConfigLayerInput(
        dataset=background_dataset,
        asset=background_dataset.assets['high_res'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=['unzip', '{input_dir}/*.zip', '-d', '{output_dir}'],
        ),
        *warp_and_cut(
            input_file='{input_dir}/NE2_HR_LC_SR_W/NE2_HR_LC_SR_W.tif',
            output_file='{output_dir}/warped_and_cut.tif',
            reproject_args=[
                '-tr', '500', '500',
                # TODO import project config and access correct boundary.
                '-te', '-5774572.727595 -5774572.727595 5774572.727595 5774572.727595',
                '-dstnodata', '0',
                '-wo', 'SOURCE_EXTRA=100',
                '-wo', 'SAMPLE_GRID=YES',
            ],
            cut_file='{assets_dir}/latitude_shape_40_degrees.geojson',
        ),
        *build_overviews(
            input_file='{input_dir}/warped_and_cut.tif',
            output_file='{output_dir}/overviews.tif',
        ),
    ],
)
