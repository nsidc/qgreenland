from typing import List

from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep


def warp_and_cut(
    *,
    # TODO: think about how to require all step template functions to take
    # input_file, output_file.
    input_file,
    output_file,
    cut_file,
    reproject_args=(),
    cut_args=(),
) -> List[ConfigLayerCommandStep]:
    reproject = ConfigLayerCommandStep(
        args=[
            'gdalwarp',
            '-t_srs', project.crs,  # dstCRS
            *reproject_args,
            f'{input_file}',  # <--- Input
            '{output_dir}/warped.tif',  # <--- Output
        ],
    )

    cut = ConfigLayerCommandStep(
        args=[
            'gdalwarp',
            '-cutline',  # CutlineDSName
            f'{cut_file}',
            '-crop_to_cutline',  # CropToCutline=True
            '-co', 'COMPRESS=DEFLATE',  # creationOptions=['COMPRESS=DEFLATE']
            *cut_args,
            '{input_dir}/warped.tif',  # <--- Input
            f'{output_file}',  # <--- Output
        ],
    )

    return [
        reproject,
        cut,
    ]
