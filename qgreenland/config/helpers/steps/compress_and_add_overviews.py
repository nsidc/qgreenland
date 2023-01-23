from typing import Literal, Optional

from qgreenland._typing import StepArgs
from qgreenland.models.config.step import AnyStep, CommandStep

# https://gdal.org/programs/gdaladdo.html
ResamplingAlgorithm = Literal[
    "nearest",
    "average",
    "rms",
    "bilinear",
    "gauss",
    "cubic",
    "cubicspline",
    "lanczos",
    "average_magphase",
    "mode",
]
CompressionType = Literal[
    "DEFLATE",
    "JPEG",
]


def compress_and_add_overviews(
    *,
    input_file: str,
    output_file: str,
    dtype_is_float: Optional[bool] = None,
    resampling_algorithm: ResamplingAlgorithm = "average",
    compress_type: CompressionType = "DEFLATE",
    compress_args: StepArgs = (),
) -> list[AnyStep]:
    """Compress raster and build overviews.

    If `dtype_is_float`, we use floating-point prediction with our compression,
    otherwise we use horizontal differencing.

            https://gdal.org/drivers/raster/gtiff.html
    """
    dtype_unexp_not_passed = compress_type == "DEFLATE" and dtype_is_float is None
    dtype_unexp_passed = compress_type != "DEFLATE" and dtype_is_float is not None
    if dtype_unexp_passed or dtype_unexp_not_passed:
        raise RuntimeError(
            "`dtype_is_float` may only be specified for DEFLATE compression" " type.",
        )

    compress_creation_options = [
        "-co",
        "TILED=YES",
        "-co",
        f"COMPRESS={compress_type}",
    ]
    if compress_type == "DEFLATE":
        predictor_value = 3 if dtype_is_float else 2
        compress_creation_options.extend(
            [
                "-co",
                f"PREDICTOR={predictor_value}",
            ]
        )

    compress = [
        "gdal_translate",
        *compress_creation_options,
        *compress_args,
        input_file,
        "{output_dir}/compressed.tif",
    ]

    copy_into_place = [
        "cp",
        "{input_dir}/compressed.tif",
        output_file,
    ]

    add_overviews = [
        "gdaladdo",
        "-r",
        resampling_algorithm,
        output_file,
        "2",
        "4",
        "8",
        "16",
    ]

    return [
        CommandStep(
            id="compress_raster",
            args=compress,
        ),
        CommandStep(
            id="build_overviews",
            args=copy_into_place + ["&&"] + add_overviews,
        ),
    ]
