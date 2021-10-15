from qgreenland.models.config.step import AnyStep, ConfigLayerCommandStep


def build_overviews(*, input_file, output_file) -> list[AnyStep]:
    copy_into_place = [
        'cp',
        f'{input_file}',
        f'{output_file}',
    ]

    add_overviews = [
        'gdaladdo',
        '-r',
        'average',
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
