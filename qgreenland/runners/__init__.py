"""A runner is a function which executes a certain type of step."""

from typing import Any

from qgreenland.models.config.step import AnyStep, CommandStep
from qgreenland.runners.command import command_runner

# Each runner corresponds to a type of "step" available in the layer
# configuration file.
RUNNERS: dict[type[AnyStep], Any] = {
    CommandStep: command_runner,
    # 'python': 'TODO',
}


def step_runner(
    step: AnyStep,
    *,
    input_dir: str,
    output_dir: str,
):
    """Execute a runner based on the step configuration."""
    RUNNERS[type(step)](
        step,
        input_dir=input_dir,
        output_dir=output_dir,
    )
