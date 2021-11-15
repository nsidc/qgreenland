from qgreenland.models.config.step import AnyStep, CommandStep


def compress_raster(
    *,
    input_file,
    output_file,
) -> list[AnyStep]:
    return [CommandStep(
        args=[
            'gdal_translate',
            '-co', 'COMPRESS=DEFLATE',
            input_file,
            output_file,
        ],
    )]
