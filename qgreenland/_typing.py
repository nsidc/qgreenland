"""QGreenland type definitions.

NOTE: This module is named strangely to avoid conflicts with the stdlib's
`types` module.
"""
from typing import Any, Dict, Literal


StepType = Literal['command', 'python']
# TODO: A better interface for steps and everything else. Pydantic models?
# Dataclasses?
Step = Dict[str, Any]
