from qgreenland._typing import QgrStr
from qgreenland.models.config.step import ConfigLayerCommandStep
from qgreenland.util.misc import run_ogr_command
from qgreenland.util.runtime_vars import EvalStr


def _interpolate_args(
    args: list[QgrStr],
    **kwargs,
) -> list[QgrStr]:
    """Replace slugs in `args` with keys and values in `kwargs`."""
    return [
        arg.eval(**kwargs) if type(arg) is EvalStr else arg
        for arg in args
    ]


def command_runner(
    step: ConfigLayerCommandStep,
    *,
    input_dir: str,
    output_dir: str,
) -> None:
    """Run a shell command in the "gdal" conda environment.

    `kwargs` are string-interpolated for each of the command's arguments.
    """
    # TODO: Some better data structure; this access is confusing.
    command_args = _interpolate_args(
        step.args,
        input_dir=input_dir,
        output_dir=output_dir,
    )

    # TODO: What's an "ogr" command? Any command will work, this just runs the
    # command in our special "gdal" conda environment. Rename the "gdal"
    # environment to the "command" environment? Rename the function to
    # "run_conda_command"? ¯\_(ツ)_/¯
    run_ogr_command(command_args)
