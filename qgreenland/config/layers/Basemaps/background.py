from qgreenland.config.datasets.background import background as background_dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


background = ConfigLayer(
    id='background',
    title='Background (500m)',
    description='Stylized shaded-relief map for providing a general sense of geography.',
    tags=['background', 'shaded-relief'],
    show=True,
    input=ConfigLayerInput(
        dataset=background_dataset,
        asset=background_dataset.assets['high_res'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/*.zip',
        ),
        *warp_and_cut(
            input_file='{input_dir}/NE2_HR_LC_SR_W.tif',
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
