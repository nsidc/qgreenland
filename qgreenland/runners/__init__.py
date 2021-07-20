"""A runner is a chainable Luigi Task which performs some type of operation.

"""

from typing import Any, Dict, Literal

# TODO: Not a Luigi.Task anymore, make functions instead.
from qgreenland.runners.command import command_runner
from qgreenland.types import Step, StepType


# Each runner corresponds to a type of "step" available in the layer
# configuration file.
RUNNERS: Dict[StepType, Any] = {
    'command': command_runner,
    'python': 'TODO',
    'template': 'TODO',
}

def step_runner(
    # TODO: Extract step type?
    step: Step,
    *,
    input_dir: str,
    output_dir: str,
):
    """Execute a runner based on the step configuration."""
    step_type = step.keys()[0]
    RUNNERS[step_type](step, input_dir=input_dir, output_dir=output_dir)
