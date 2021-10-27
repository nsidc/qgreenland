from abc import ABC, abstractmethod
from functools import cached_property
from typing import Optional, Union

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr


class ConfigLayerStep(ABC):
    id: Optional[str]

    type: str

    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    # TODO: Why do I have to re-specify `id` when it's already defined in the
    # ABC?
    id: Optional[str]

    type: str = 'command'

    args: list[EvalStr]

    @cached_property
    def provenance(self) -> str:
        return ' '.join([str(arg) for arg in self.args])


AnyStep = Union[ConfigLayerCommandStep]
