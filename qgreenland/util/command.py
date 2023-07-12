import logging
import subprocess
from collections.abc import Sequence

import qgreenland.exceptions as exc
from qgreenland.constants.project import ENV_MANAGER
from qgreenland.util.runtime_vars import EvalStr

logger = logging.getLogger("luigi-interface")


def interpolate_args(
    args: Sequence[EvalStr],
    **kwargs,
) -> list[str]:
    """Replace slugs in `args` with keys and values in `kwargs`."""
    return [arg.eval(**kwargs) for arg in args]


def run_qgr_command(args: list[str]) -> None:
    """Run a command in the `qgreenland-cmd` environment."""
    conda_env_name = "qgreenland-cmd"
    # With conda or mamba, `. activate myenv` works as expected, but with micromamba, we
    # need something a little different.
    if ENV_MANAGER == "micromamba":
        cmd = [
            "eval",
            '"$(micromamba shell hook -s posix)"',
            "&&",
            "micromamba",
            "activate",
            conda_env_name,
            "&&",
            *args,
        ]

    else:
        cmd = [".", "activate", conda_env_name, "&&", *args]

    run_cmd(cmd)
    return


def run_cmd(args: list[str]) -> subprocess.CompletedProcess:
    """Run a command and log it."""
    # Hack. The activation of a conda environment does not work without `shell=True`.
    cmd_str = " ".join(str(arg) for arg in args)

    logger.info("Running command:")
    logger.info(cmd_str)
    result = subprocess.run(
        cmd_str,
        shell=True,
        executable="/bin/bash",
        capture_output=True,
    )

    if result.returncode != 0:
        stdout = str(result.stdout, encoding="utf8")
        stderr = str(result.stderr, encoding="utf8")
        output = f"===STDOUT===\n{stdout}\n\n===STDERRR===\n{stderr}"
        raise exc.QgrSubprocessError(
            f"Subprocess failed with output:\n\n{output}",
        )

    return result
