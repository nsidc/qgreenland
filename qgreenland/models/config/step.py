from abc import ABC, abstractmethod
from functools import cached_property
from typing import List, Literal, Union

from qgreenland.models.base_model import QgrBaseModel


class ConfigLayerStep(ABC):
    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    # input_file: Path
    # output_file: Path
    args: List[str]

    # If template:
    # template_name: str
    # kwargs: Dict[str, Any]

    # If command:
    # args: List[str, int]

    # If Python:
    # kwargs: Dict[str, Any]

    @cached_property
    def provenance(self) -> str:
        return ' '.join(self.args)


AnyStep = Union[ConfigLayerCommandStep]
