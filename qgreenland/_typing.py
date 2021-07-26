# NOTE: Will naming this module "types.py" cause a weird conflict?
from typing import Any, Dict, Literal


StepType = Literal['command', 'python', 'template']
# TODO: Make this into an interface that specifies only one top-level key
Step = Dict[StepType, Dict[str, Any]]
