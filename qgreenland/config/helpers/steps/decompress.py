from typing import Literal

from qgreenland.models.config.step import ConfigLayerCommandStep


def decompress_step(
    *,
    input_file: str,
    decompress_type: Literal['unzip', '7z'] = 'unzip',
    decompress_contents_mask: str = '',
) -> ConfigLayerCommandStep:
    if decompress_type == 'unzip':
        return ConfigLayerCommandStep(
            args=[
                'unzip',
                input_file,
                '-d', '{output_dir}',
                decompress_contents_mask,
            ],
        )
    elif decompress_type == '7z':
        return ConfigLayerCommandStep(
            args=[
                '7z',
                'x', input_file,
                '-o{output_dir}',
                decompress_contents_mask,
            ],
        )
    else:
        raise NotImplementedError(
            f'Unexpected decompress type: {decompress_type}.',
        )
