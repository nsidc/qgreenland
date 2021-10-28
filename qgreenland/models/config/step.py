from abc import ABC, abstractmethod
from functools import cached_property
from typing import Optional, Union

from pydantic import root_validator

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

    # Not sure why, but we can't get this to work with a regular validator.
    @root_validator
    @classmethod
    def set_default_id(cls, values):
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


AnyStep = Union[ConfigLayerCommandStep]
