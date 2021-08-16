from abc import ABC, abstractmethod
from functools import cached_property
from typing import List, Literal, Union

from qgreenland.models.base_model import QgrBaseModel


class ConfigLayerStep(ABC):
    @abstractmethod
    def provenance(self) -> str:
        pass


class ConfigLayerCommandStep(QgrBaseModel, ConfigLayerStep):
    type: Literal['command']

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

    # @cache
    # def _provenance_text(self) -> str:
    #     return 'foo'

    # TODO: ABC for COnfigLayerStep, subclasses for command, python func.
    @cached_property
    def provenance(self) -> str:
        return ' '.join(self.args)


AnyStep = Union[ConfigLayerCommandStep]
