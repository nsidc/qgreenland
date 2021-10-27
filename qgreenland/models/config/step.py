from abc import ABC, abstractmethod
from functools import cached_property
from typing import Optional, Union

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr


class ConfigLayerStep(ABC):
    name: Optional[str]
    type: str

    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    # TODO: Validate contains no spaces or slashes
    id: str = 'command'

    args: list[EvalStr]

    @cached_property
    def provenance(self) -> str:
        return ' '.join([str(arg) for arg in self.args])


AnyStep = Union[ConfigLayerCommandStep]
