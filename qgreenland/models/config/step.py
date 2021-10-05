from abc import ABC, abstractmethod
from functools import cached_property
from typing import Union, cast

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr


class ConfigLayerStep(ABC):
    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    # TODO: Remove the "type" field?
    type: str = 'command'
    # input_file: Path
    # output_file: Path

    # If command:
    args: list[EvalStr]

    # If template:
    # template_name: str
    # kwargs: Dict[str, Any]

    # If Python:
    # kwargs: Dict[str, Any]

    @cached_property
    def provenance(self) -> str:
        return ' '.join([str(arg) for arg in self.args])


AnyStep = Union[ConfigLayerCommandStep]
