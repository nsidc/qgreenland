from qgreenland.config.datasets.background import background as background_dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import compress_and_add_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


def _separate_band(idx) -> list[str]:
    return [
        'gdal_translate',
        '-b', str(idx),
        '{input_dir}/input.tif',
        '{output_dir}/' + f'b{idx}.tif',
    ]


background = Layer(
    id='background',
    title='Background (500m)',
    description='Stylized shaded-relief map for providing a general sense of geography.',
    tags=['background', 'shaded-relief'],
    show=True,
    input=LayerInput(
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
        # Because the background image is large, we use JPEG compression
        # (`compress_and_add_overviews` step below). To do so without JPEG
        # artifacts around the edges of the image (appears as black pixels
        # around the outside edges of the image), a mask band can be
        # used. This step creates the mask file that will be added as a fourth
        # band to the RGB background image.
        CommandStep(
            id='create_mask',
            args=[
                'cp', '{input_dir}/warped_and_cut.tif', '{output_dir}/input.tif',
                '&&',
                'gdal_calc.py',
                '--calc="numpy.invert(numpy.isnan(A)).astype(int)"',
                '--outfile={output_dir}/mask.tif',
                '-A', '{output_dir}/input.tif',
                '--A_band=1',
            ],
        ),
        # The next step uses `gdal_merge.py` to combine the background image
        # with the mask to create the 4 band raster. This step separates the
        # input file's bands (R, G, B) into three separate files (b1.tif,
        # b2.tif, b3.tif) that can be used by `gdal_merge.py`. NOTE: this step
        # is not strictly necessary but substantially speeds up the merge
        # operation. Without splitting into individual bands, the `gdal_merge`
        # operation takes ~1 hour to complete vs ~40 seconds when the bands are
        # pre-separated.
        CommandStep(
            id='separate_bands',
            args=[
                'cp', '{input_dir}/*', '{output_dir}/',
                '&&',
                *_separate_band(1),
                '&&',
                *_separate_band(2),
                '&&',
                *_separate_band(3),
            ],
        ),
        # Merge the RGB + mask geotiffs into one, 4 band raster file.
        CommandStep(
            id='merge_bands',
            args=[
                'gdal_merge.py',
                '-o', '{output_dir}/merged.tif',
                '-co', 'COMPRESS=DEFLATE',
                '-separate',
                '{input_dir}/b1.tif',
                '{input_dir}/b2.tif',
                '{input_dir}/b3.tif',
                '{input_dir}/mask.tif',
            ],
        ),
        # Finally, add compression with overviews and use the newly added band 4
        # as a mask.
        *compress_and_add_overviews(
            input_file='{input_dir}/merged.tif',
            output_file='{output_dir}/overviews.tif',
            compress_type='JPEG',
            compress_args=[
                '-co', 'JPEG_QUALITY=90',
                '-co', 'PHOTOMETRIC=YCBCR',
                '-b', '1', '-b', '2', '-b', '3',
                # The `-mask 4` option sets band 4 as the mask.
                '-mask', '4',
                '--config', 'GDAL_TIFF_INTERNAL_MASK', 'YES',
            ],
        ),
    ],
)
