import inspect
from functools import cached_property
from typing import Any

from pydantic import (
    BaseModel,
    Extra,
    validator,
)


class QgrBaseModel(BaseModel):
    """Implements 'faux' immutability and allows usage of `functools.cached_property`.

    Immutability is not 'strict' (e.g., dicts can be mutated) - a
    determined dev can still mutate model instances.
    """

    @validator('*')
    @classmethod
    def clean_all_string_fields(cls, value):
        """Clean up all string fields with `cleandoc`.

        This adjusts indentation and removes leading and trailing newlines, enabling
        cleaner use of triple-quoted strings, just like docstrings.
        """
        if isinstance(value, str):
            return inspect.cleandoc(value)
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
