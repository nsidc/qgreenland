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
    #TODO: Use fiona to get a bbox from the cutfile?

    reproject = ConfigLayerCommandStep(
        type='command',
        args=[
            'gdalwarp',
            '-t_srs',  # dstCRS
            PROJECT_CRS,
            *reproject_args,
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
