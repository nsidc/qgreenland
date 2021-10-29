from qgreenland._typing import StepArgs
from qgreenland.models.config.step import ConfigLayerCommandStep


def gdal_edit(
    *,
    input_file: str,
    output_file: str,
    gdal_edit_args: StepArgs = (),
) -> list[ConfigLayerCommandStep]:

    return [ConfigLayerCommandStep(
        id='gdal_edit',
        args=[
            'cp', input_file, output_file,
            '&&',
            'gdal_edit.py',
            *gdal_edit_args,
            output_file,
        ],
    )]
