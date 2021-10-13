from typing import Literal

from qgreenland.models.config.step import ConfigLayerCommandStep


def decompress_step(
    *,
    input_file: str,
    decompress_type: Literal['unzip'] = 'unzip',
    decompress_contents_mask: str = '',
) -> ConfigLayerCommandStep:
    if decompress_type != 'unzip':
        raise NotImplementedError(
            f'Unexpected decompress type: {decompress_type}.',
        )

    return ConfigLayerCommandStep(
        args=[
            'unzip',
            input_file,
            '-d', '{output_dir}',
            decompress_contents_mask,
        ],
    )
