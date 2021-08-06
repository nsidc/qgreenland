"""A runner is a function which executes a certain type of step."""

from typing import Any, Dict

from qgreenland._typing import ConfigStepType
from qgreenland.models.config.step import ConfigLayerStep
from qgreenland.runners.command import command_runner


# Each runner corresponds to a type of "step" available in the layer
# configuration file.
RUNNERS: Dict[ConfigStepType, Any] = {
    'command': command_runner,
    'python': 'TODO',
}


def step_runner(
    step: ConfigLayerStep,
    *,
    input_dir: str,
    output_dir: str,
):
    """Execute a runner based on the step configuration."""
    RUNNERS[step.type](
        step,
        input_dir=input_dir,
        output_dir=output_dir,
    )
