from typing import List

from qgreenland.models.config.step import AnyStep, ConfigLayerCommandStep
from qgreenland.config.constants import PROJECT_CRS


def warp_and_cut(
        *,
        # TODO: think about how to require all step template functions to take
        # input_file, output_file.
        input_file,
        output_file,
        x_res,
        y_res,
        target_extent,
        cut_file,
) -> List[AnyStep]:
    reproject = ConfigLayerCommandStep(
        type='command',
        args=[
            'gdalwarp',
            '-t_srs',  # dstCRS
            PROJECT_CRS,
            '-tr',  # xRes=500, yRes=500
            f'{x_res}',
            f'{y_res}',
            '-te',
            f'{target_extent}',
            '-dstnodata',  # dstNodata
            '0',
            '-wo',  # warpOptions=['SOURCE_EXTRA=100', 'SAMPLE_GRID=YES']
            'SOURCE_EXTRA=100',
            '-wo',
            'SAMPLE_GRID=YES',
            # What about using dedicated keys for `input_file` and `output_file` so
            # the command itself can reference that slug. If either is repeated in5
            # the command, this will help avoid mistakes.
            f'{input_file}',  # <--- Input
            '{output_dir}/warped.tif',  # <--- Output
        ],
    )

    clip = ConfigLayerCommandStep(
        # TODO: Do we have to spec 'command' here?
        type='command',
        args=[
            'gdalwarp',
            '-cutline',  # CutlineDSName
             # TODO: Abstract boundaries... as slugs? e.g.:
             #     {boundaries.background.filepath}
            f'{cut_file}',
            '-crop_to_cutline',  # CropToCutline=True
            '-co',  # creationOptions=['COMPRESS=DEFLATE']
            'COMPRESS=DEFLATE',
            '{input_dir}/warped.tif',  # <--- Input
            f'{output_file}',  # <--- Output
        ],
    )

    return [
        reproject,
        clip,
    ]
