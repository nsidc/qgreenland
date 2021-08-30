from typing import List

from qgreenland.models.config.step import AnyStep, ConfigLayerCommandStep
from qgreenland.config.constants import PROJECT_CRS


def warp_and_cut(
        *,
        # TODO: think about how to require all step template functions to take
        # input_file, output_file.
        input_file,
        output_file,
        cut_file,
        reproject_args=[],
        cut_args=[],
) -> List[AnyStep]:
    reproject = ConfigLayerCommandStep(
        type='command',
        args=[
            'gdalwarp',
            '-t_srs',  # dstCRS
            PROJECT_CRS,
            *reproject_args,
            # What about using dedicated keys for `input_file` and `output_file` so
            # the command itself can reference that slug. If either is repeated in5
            # the command, this will help avoid mistakes.
            f'{input_file}',  # <--- Input
            '{output_dir}/warped.tif',  # <--- Output
        ],
    )

    cut = ConfigLayerCommandStep(
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
            *cut_args,
            '{input_dir}/warped.tif',  # <--- Input
            f'{output_file}',  # <--- Output
        ],
    )

    return [
        reproject,
        cut,
    ]
