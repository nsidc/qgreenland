from types import MappingProxyType

from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep


# Create an immutable dict for the decompress step kwargs default value (flake8
# B006 and B008)
default_decompress_step_kwargs: MappingProxyType[None, None] = MappingProxyType({})


# TODO: Make it more generic? Compressed vector? How can we compose
# step-generation functions?
# TODO: Do we need to run ogr2ogr with -makevalid in some cases? Use a parameter
# to trigger it?
def zipped_vector(
    *,
    input_file: str,
    output_file: str,
    vector_filename: str = '*.shp',
    decompress_step_kwargs=default_decompress_step_kwargs,
    ogr2ogr_args: tuple[str, ...] = (),
) -> list[ConfigLayerCommandStep]:
    """Unzip a vector data file and reproject."""
    return [
        decompress_step(
            input_file=input_file,
            **decompress_step_kwargs,
        ),
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                *ogr2ogr_args,
                '-clipdst', project.boundaries['background'].filepath,
                output_file,
                '{input_dir}/' + vector_filename,
            ],
        ),
    ]
