from typing import Optional

from qgreenland.constants import ANCILLARY_DIR, ASSETS_DIR


def interpolate_runtime_vars(
    string: str,
    *,
    input_dir: Optional[str] = None,
    output_dir: Optional[str] = None,
) -> str:
    """Interpolate runtime configuration slugs with values.

    `{ancillary_dir}` is interpolated with the value of `constants.ANCILLARY_DIR`.
    `{assets_dir}` is interpolated with the value of `constants.ASSETS_DIR`.

    Optionally, interpolate `{input_dir}` and `{output_dir}` with the value of
    corresponding kwargs.
    """
    return string.format(
        input_dir=input_dir,
        output_dir=output_dir,
        assets_dir=ASSETS_DIR,
        ancillary_dir=ANCILLARY_DIR,
    )
