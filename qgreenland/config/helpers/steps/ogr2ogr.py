from qgreenland.config.project import project
from qgreenland.util.runtime_vars import EvalFilePath

STANDARD_OGR2OGR_ARGS = [
    '-lco', 'ENCODING=UTF-8',
    '-t_srs', project.crs,
]


def ogr2ogr(
    *,
    input_file: str,
    output_file: str,
    boundary_filepath: EvalFilePath = project.boundaries['background'].filepath,
    ogr2ogr_args: tuple[str, ...] = (),
) -> List[ConfigLayerCommandStep]:
    """Warp to project CRS and do other stuff as specified in args."""
    return [ConfigLayerCommandStep(
        args=[
            'ogr2ogr',
            *STANDARD_OGR2OGR_ARGS,
            '-clipdst', project.boundaries['data'].filepath,
            '-makevalid',
            *ogr2ogr_args,
            output_file,
            input_file,
        ],
    )]
