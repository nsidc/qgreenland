from functools import cached_property

from pydantic import BaseModel


class ImmutableBaseModel(BaseModel):
    """Implements 'faux' immutability on models that inherit from this class.

    See https://pydantic-docs.helpmanual.io/usage/models/#faux-immutability

    This immutability is not 'strict' (e.g., dicts can be mutated) - a
    determined dev can still mutate model instances.
    """

    class Config:
        allow_mutation = False
        keep_untouched = (cached_property,)
