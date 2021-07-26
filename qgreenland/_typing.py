"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Any, Dict, Literal


StepType = Literal['command', 'python']
# TODO: Make this into an interface that specifies only one top-level key
Step = Dict[StepType, Dict[str, Any]]
