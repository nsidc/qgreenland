from abc import ABC, abstractmethod
from functools import cached_property
from typing import Literal, Optional, Union

from pydantic import root_validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr


class LayerStep(ABC):
    id: Optional[str]
    """An identifier for the step. Does not need to be unique."""

    type: str
    """The type of the step. Should not be set by the user."""

    @abstractmethod
    @cached_property
    def provenance(self) -> str:
        """Represent what was done in this step."""
        pass


class CommandStep(QgrBaseModel, LayerStep):
    """A step run as a shell command."""

    # TODO: Why do I have to re-specify `id` when it's already defined in the
    # ABC?
    id: Optional[str]

    # TODO: How to prevent this from being overridden at instantiation time?
    type: Literal['command'] = 'command'

    args: list[EvalStr]
    """The command arguments, e.g. ['cat', '{input_dir}/foo.txt']."""  # noqa:FS003

    # We use a root validator here because with a regular validator, we would
    # not have access to the `args` field, because field order matters to
    # regular validators. We didn't want to order our fields based on validator
    # dependencies.
    @root_validator
    @classmethod
    def set_default_id(cls, values):
        """Generate an identifier from `args` if one is not provided."""
        if 'id' in values and values['id'] is not None:
            return values

        text = values['args'][0].lower()

        symbols = [' ', '-', '=', '\\', '.']
        for symbol in symbols:
            if symbol in text:
                text = text.replace(symbol, '_')

        values['id'] = text
        return values

    @cached_property
    def provenance(self) -> str:
        return ' '.join([str(arg) for arg in self.args])


AnyStep = Union[CommandStep]
