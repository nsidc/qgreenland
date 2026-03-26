from qgreenland.models.config.step import PythonStep
from qgreenland.util.command import run_qgr_command


def python_runner(
    step: PythonStep,
    *,
    input_dir: str,
    output_dir: str,
) -> None:
    """Run a Python function in the "qgreenland-cmd" conda environment."""
    function = step.function
    module = function.__module__
    name = function.__qualname__

    import_str = f"from {module} import {name}"

    allow_breakpoint = "breakpoint()" in step.provenance

    run_qgr_command(
        [
            "python",
            "-c",
            f"\"{import_str}; {name}(input_dir='{input_dir}', output_dir='{output_dir}')\"",  # noqa
        ],
        allow_breakpoint=allow_breakpoint,
    )

    if allow_breakpoint:
        # raise an error at this point if a breakpoint is detected. We want to
        # ensure breakpoints do not remain in the code in prod configurations.
        raise RuntimeError(
            "Breakpoint detected in `{module}.{name}`. Remove to continue."
        )
