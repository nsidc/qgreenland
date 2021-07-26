"""A runner is a function which executes a certain type of step."""

from typing import Any, Dict, Literal

# TODO: Not a Luigi.Task anymore, make functions instead.
from qgreenland.runners.command import command_runner
from qgreenland._typing import Step, StepType


# Each runner corresponds to a type of "step" available in the layer
# configuration file.
RUNNERS: Dict[StepType, Any] = {
    'command': command_runner,
    'python': 'TODO',
    'template': 'TODO',
}

def step_runner(
    step: Step,
    *,
    input_dir: str,
    output_dir: str,
):
    """Execute a runner based on the step configuration."""
    # TODO: Improve Step API
    step_type = list(step.keys())[0]
    RUNNERS[step_type](step, input_dir=input_dir, output_dir=output_dir)
