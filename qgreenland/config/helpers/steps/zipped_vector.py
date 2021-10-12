from qgreenland.config.helpers.steps.ogr2ogr import (
    STANDARD_OGR2OGR_ARGS,
)
from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep


# TODO: Make it more generic? Compressed vector? How can we compose
# step-generation functions?
# TODO: Do we need to run ogr2ogr with -makevalid in some cases? Use a parameter
# to trigger it?
def zipped_vector(
    *,
    input_file: str,
    output_file: str,
    shapefile_name: str = '*.shp',
    ogr2ogr_args: tuple[str, ...] = (),
) -> list[ConfigLayerCommandStep]:
    """Unzip standard shapefile and reproject."""
    return [
        ConfigLayerCommandStep(
            args=[
                'unzip',
                input_file,
                '-d', '{output_dir}',
            ],
        ),
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                *STANDARD_OGR2OGR_ARGS,
                *ogr2ogr_args,
                '-clipdst', project.boundaries['background'].filepath,
                output_file,
                '{input_dir}/' + shapefile_name,
            ],
        ),
    ]
