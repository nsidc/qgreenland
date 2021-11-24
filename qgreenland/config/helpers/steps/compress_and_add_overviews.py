from typing import Literal

from qgreenland.models.config.step import AnyStep, CommandStep

# https://gdal.org/programs/gdaladdo.html
ResamplingAlgorithm = Literal[
    'nearest',
    'average',
    'rms',
    'bilinear',
    'gauss',
    'cubic',
    'cubicspline',
    'lanczos',
    'average_magphase',
    'mode',
]
CompressionType = [
    'DEFLATE',
    'JPEG',
]


def compress_and_add_overviews(
    *,
    input_file: str,
    output_file: str,
    # TODO: This parameter is ignored if the compression type isn't deflate.
    # Refactor args?
    dtype_is_float: bool,
    resampling_algorithm: ResamplingAlgorithm = 'average',
    compression_type: CompressionType = 'DEFLATE',
) -> list[AnyStep]:
    """Compress raster and build overviews.

    If `dtype_is_float`, we use floating-point prediction with our compression,
    otherwise we use horizontal differencing.

            https://gdal.org/drivers/raster/gtiff.html
    """
    compress_creation_options = [
        '-co', 'TILED=YES',
        '-co', f'COMPRESS={compression_type}',
    ]
    if compression_type == 'DEFLATE':
        predictor_value = 3 if dtype_is_float else 2
        compress_creation_options.extend([
            '-co',
            f'PREDICTOR={predictor_value}',
        ])

    compress = [
        'gdal_translate',
        *compress_creation_options,
        input_file,
        '{output_dir}/compressed.tif',
    ]

    copy_into_place = [
        'cp',
        '{input_dir}/compressed.tif',
        output_file,
    ]

    add_overviews = [
        'gdaladdo',
        '-r', resampling_algorithm,
        output_file,
        '2',
        '4',
        '8',
        '16',
    ]

    return [
        CommandStep(
            id='compress_raster',
            args=compress,
        ),
        CommandStep(
            id='build_overviews',
            args=copy_into_place + ['&&'] + add_overviews,
        ),
    ]
