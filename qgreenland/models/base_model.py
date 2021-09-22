from functools import cached_property
from typing import Any

from pydantic import BaseModel, Extra, validator

from qgreenland.util.model.validate import clean_string


class QgrBaseModel(BaseModel):
    """Implements 'faux' immutability and allows usage of `functools.cached_property`.

    Immutability is not 'strict' (e.g., dicts can be mutated) - a
    determined dev can still mutate model instances.
    """

    @validator('*')
    @classmethod
    def clean_all_string_fields(cls, value):
        if isinstance(value, str):
            return clean_string(value)
        return value

    class Config:
        # Throw an error if any unexpected attrs are provided. default: 'ignore'
        extra = Extra.forbid

        # https://pydantic-docs.helpmanual.io/usage/models/#faux-immutability
        allow_mutation = False

        # https://github.com/samuelcolvin/pydantic/issues/1241
        # https://github.com/samuelcolvin/pydantic/issues/2763
        keep_untouched = (cached_property,)

        arbitrary_types_allowed = True

    def __json__(self) -> dict[Any, Any]:
        return self.dict()
