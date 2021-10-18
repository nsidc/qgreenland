from typing import Literal

from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: make this return a list of one step like e.g., build_overviews?
def decompress_step(
    *,
    input_file: str,
    decompress_type: Literal['unzip', '7z', 'gzip'] = 'unzip',
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
    elif decompress_type == 'gzip':
        return ConfigLayerCommandStep(
            args=[
                'cp', input_file, '{output_dir}/',
                '&&',
                'gzip',
                '-d',
                '{output_dir}/*.gz',
            ],
        )

    else:
        raise NotImplementedError(
            f'Unexpected decompress type: {decompress_type}.',
        )
