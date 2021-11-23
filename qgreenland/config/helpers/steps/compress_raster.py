# TODO: DELETE ME
from qgreenland.models.config.step import AnyStep, CommandStep


def compress_raster(
    *,
    input_file: str,
    output_file: str,
) -> list[AnyStep]:
    return [CommandStep(
        args=[
            'gdal_translate',
            '-co', 'COMPRESS=DEFLATE',
            # TODO: `-co TILED=yes`
            input_file,
            output_file,
        ],
    )]
