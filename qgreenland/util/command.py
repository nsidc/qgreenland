from typing import Sequence

from qgreenland.util.runtime_vars import EvalStr


def interpolate_args(
    args: Sequence[EvalStr],
    **kwargs,
) -> list[str]:
    """Replace slugs in `args` with keys and values in `kwargs`."""
    return [arg.eval(**kwargs) for arg in args]
