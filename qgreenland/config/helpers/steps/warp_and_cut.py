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
) -> list[ConfigLayerCommandStep]:
    reproject = ConfigLayerCommandStep(
        args=[
            'gdalwarp',
            '-t_srs', project.crs,
            *reproject_args,
            f'{input_file}',
            '{output_dir}/warped.tif',
        ],
    )

    cut = ConfigLayerCommandStep(
        args=[
            'gdalwarp',
            '-cutline',
            f'{cut_file}',
            '-crop_to_cutline',
            '-co', 'COMPRESS=DEFLATE',
            *cut_args,
            '{input_dir}/warped.tif',
            f'{output_file}',
        ],
    )

    return [
        reproject,
        cut,
    ]
