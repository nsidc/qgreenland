from qgreenland._typing import ResamplingMethod, StepArgs
from qgreenland.config.project import project
from qgreenland.models.config.step import CommandStep
from qgreenland.util.runtime_vars import EvalFilePath


def warp(
    *,
    input_file: str,
    output_file: str,
    cut_file: EvalFilePath,
    resampling_method: ResamplingMethod = "bilinear",
    warp_args: StepArgs = (),
) -> list[CommandStep]:
    return [
        CommandStep(
            args=[
                "gdalwarp",
                "-cutline",
                cut_file,
                "-crop_to_cutline",
                "-r",
                resampling_method,
                "-t_srs",
                project.crs,
                *warp_args,
                "-co",
                "COMPRESS=DEFLATE",
                input_file,
                output_file,
            ],
        )
    ]
