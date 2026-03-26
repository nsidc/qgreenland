from abc import ABC, abstractmethod
from functools import cached_property
from typing import Literal, Optional, Protocol, Union, runtime_checkable

from pydantic import root_validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr
from qgreenland.util.version import get_build_version


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


def _prepare_text_for_id(text: str) -> str:
    symbols = [" ", "-", "=", "\\", ".", ":"]
    for symbol in symbols:
        if symbol in text:
            text = text.replace(symbol, "_")

    return text


class CommandStep(QgrBaseModel, LayerStep):
    """A step run as a shell command."""

    # TODO: Why do I have to re-specify `id` when it's already defined in the
    # ABC?
    id: Optional[str]

    # TODO: How to prevent this from being overridden at instantiation time?
    type: Literal["command"] = "command"

    args: list[EvalStr]
    """The command arguments, e.g. ['cat', '{input_dir}/foo.txt']."""

    # We use a root validator here because with a regular validator, we would
    # not have access to the `args` field, because field order matters to
    # regular validators. We didn't want to order our fields based on validator
    # dependencies.
    @root_validator
    @classmethod
    def set_default_id(cls, values):
        """Generate an identifier from `args` if one is not provided."""
        if "id" in values and values["id"] is not None:
            return values

        text = values["args"][0].lower()

        text = _prepare_text_for_id(text)

        values["id"] = text
        return values

    @cached_property
    def provenance(self) -> str:
        return " ".join([str(arg) for arg in self.args])


# https://docs.python.org/3/library/typing.html#annotating-callable-objects
@runtime_checkable
class PythonFuncStep(Protocol):
    __qualname__: str
    __module__: str

    def __call__(self, *, input_dir: str, output_dir: str) -> None:
        ...


class PythonStep(QgrBaseModel, LayerStep):
    id: Optional[str]

    type: Literal["python"] = "python"

    function: PythonFuncStep

    @staticmethod
    def module_path(function: PythonFuncStep) -> str:
        module = function.__module__
        name = function.__qualname__

        return f"{module}:{name}"

    @root_validator
    @classmethod
    def set_default_id(cls, values):
        if "id" in values and values["id"] is not None:
            return values

        module_path = cls.module_path(values["function"])
        id_str = _prepare_text_for_id(module_path)

        values["id"] = id_str

        return values

    @cached_property
    def provenance(self) -> str:
        module = self.function.__module__
        name = self.function.__qualname__

        git_version = get_build_version()

        provenance_str = f"Python Step: {module}:{name} @ {git_version}"

        return provenance_str


AnyStep = Union[CommandStep, PythonStep]
