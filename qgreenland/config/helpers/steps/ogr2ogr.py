from typing import Any

from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep
from qgreenland.util.runtime_vars import EvalFilePath

STANDARD_OGR2OGR_ARGS = [
    '-lco', 'ENCODING=UTF-8',
    '-t_srs', project.crs,
]


# TODO: Should "enable_partial_reprojection" be a generic "env" parameter?
# Key/value mapping?
def ogr2ogr(
    *,
    input_file: str,
    output_file: str,
    boundary_filepath: EvalFilePath = project.boundaries['background'].filepath,
    ogr2ogr_args: tuple[str, ...] = (),
    enable_partial_reprojection=False,
) -> list[ConfigLayerCommandStep]:
    """Warp to project CRS and do other stuff as specified in args."""
    init_args: list[Any] = []
    if enable_partial_reprojection:
        init_args.append('OGR_ENABLE_PARTIAL_REPROJECTION=TRUE')

    return [ConfigLayerCommandStep(
        id='ogr2ogr',
        args=init_args + [
            'ogr2ogr',
            *STANDARD_OGR2OGR_ARGS,
            '-clipdst', boundary_filepath,
            '-makevalid',
            *ogr2ogr_args,
            output_file,
            input_file,
        ],
    )]
