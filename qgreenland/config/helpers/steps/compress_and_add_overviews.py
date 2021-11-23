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


def compress_and_add_overviews(
    *,
    input_file: str,
    output_file: str,
    dtype_is_float: bool,
    resampling_algorithm: ResamplingAlgorithm = 'average',
) -> list[AnyStep]:
    predictor_value = 3 if dtype_is_float else 2

    compress = [
        'gdal_translate',
        '-co', 'COMPRESS=DEFLATE',
        '-co', f'PREDICTOR={predictor_value}',
        # TODO: `-co TILED=yes`
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
            args=[
                *compress,
            ],
        ),
        CommandStep(
            id='build_overviews',
            args=[
                *copy_into_place,
                '&&',
                *add_overviews,
            ],
        ),
    ]
