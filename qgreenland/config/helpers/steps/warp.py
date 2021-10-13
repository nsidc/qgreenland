from typing import List

from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep
from qgreenland.util.runtime_vars import EvalFilePath


def warp(
    *,
    input_file: str,
    output_file: str,
    cut_file: EvalFilePath,
    warp_args: tuple[str, ...] = (),
) -> List[ConfigLayerCommandStep]:

    return [ConfigLayerCommandStep(
        args=[
            'gdalwarp',
            '-cutline',
            f'{cut_file}',
            '-crop_to_cutline',
            '-t_srs', project.crs,  # dstCRS
            *warp_args,
            '-co', 'COMPRESS=DEFLATE',
            f'{input_file}',
            f'{output_file}',
        ],
    )]
