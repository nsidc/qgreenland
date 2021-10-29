from typing import Literal

from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: make this return a list of one step like e.g., build_overviews?
def decompress_step(
    *,
    input_file: str,
    decompress_type: Literal['unzip', '7z', 'gzip'] = 'unzip',
    decompress_contents_mask: str = '',
) -> ConfigLayerCommandStep:
    args: list[str]
    if decompress_type == 'unzip':
        args = [
            'unzip',
            input_file,
            '-d', '{output_dir}',
            decompress_contents_mask,
        ]
    elif decompress_type == '7z':
        args = [
            '7z',
            'x', input_file,
            '-o{output_dir}',
            decompress_contents_mask,
        ]
    elif decompress_type == 'gzip':
        if decompress_contents_mask:
            raise NotImplementedError((
                'The `decompress_contents_mask` kwarg is not supported for'
                ' the `gzip` decompression type.'
            ))

        args = [
            'cp', input_file, '{output_dir}/',
            '&&',
            'gzip',
            '-d',
            '{output_dir}/*.gz',
        ]
    else:
        raise NotImplementedError(
            f'Unexpected decompress type: {decompress_type}.',
        )

    return ConfigLayerCommandStep(
        id=f'decompress_{decompress_type}',
        args=args,
    )
