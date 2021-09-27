from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: Make it more generic? Compressed vector? How can we compose
# step-generation functions?
def zipped_vector(
    *,
    input_file: str,
    output_file: str,
) -> list[ConfigLayerCommandStep]:
    """Simple unzip of standard shapefile and reproject."""
    return [
        ConfigLayerCommandStep(
            args=[
                'unzip',
                input_file,
            ],
        ),
        ConfigLayerCommandStep(
            args=[
                'foo',
            ],
        ),
    ]
