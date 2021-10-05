from abc import ABC, abstractmethod
from functools import cached_property
from typing import List, Union

from qgreenland.models.base_model import QgrBaseModel
from qgreenland._typing import QgrStr


class ConfigLayerStep(ABC):
    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    type: str = 'command'
    # input_file: Path
    # output_file: Path

    # If command:
    args: List[QgrStr]

    # If template:
    # template_name: str
    # kwargs: Dict[str, Any]

    # If Python:
    # kwargs: Dict[str, Any]

    @cached_property
    def provenance(self) -> str:
        return ' '.join(self.args)


AnyStep = Union[ConfigLayerCommandStep]
