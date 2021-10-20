from qgreenland.models.config.step import AnyStep, ConfigLayerCommandStep


def compress_raster(
    *,
    input_file,
    output_file,
) -> list[AnyStep]:
    return [ConfigLayerCommandStep(
        args=[
            'gdal_translate',
            '-co', 'COMPRESS=DEFLATE',
            input_file,
            output_file,
        ],
    )]
