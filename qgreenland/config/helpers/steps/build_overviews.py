from typing import Literal

from qgreenland.models.config.step import AnyStep, ConfigLayerCommandStep


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


def build_overviews(
        *,
        input_file,
        output_file,
        resampling_algorithm: ResamplingAlgorithm = 'average',
) -> list[AnyStep]:
    copy_into_place = [
        'cp',
        f'{input_file}',
        f'{output_file}',
    ]

    add_overviews = [
        'gdaladdo',
        '-r', resampling_algorithm,
        f'{output_file}',
        '2',
        '4',
        '8',
        '16',
    ]

    return [ConfigLayerCommandStep(
        args=[
            *copy_into_place,
            '&&',
            *add_overviews,
        ],
    )]
