import re
from collections import UserString
from typing import Optional, Union

from qgreenland.models.base_model import QgrBaseModel

layer_identifier_regex = re.compile(r"[a-z0-9_]*")
layer_group_identifier_regex = re.compile(r"[A-Z0-9][a-zA-Z0-9() ,._-]*")


class LayerIdentifier(UserString):
    """A string uniquely identifying a layer.

    Based on docs: https://docs.pydantic.dev/1.10/usage/types/#classes-with-__get_validators__

    TODO: The doc above specifies a `__modify_schema__` method which we're not using.
    Should we be?
    TODO: Update other models to replace string layer identifiers with this class?
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, cls):
            raise TypeError(f"Must be explicitly initialized with {cls.__name__}()")
        m = layer_identifier_regex.fullmatch(str(v))
        if not m:
            raise ValueError(f'Invalid layer identifier format "{v}"')

        return v

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"

    def __json__(self):
        """When exporting to JSON to create a "lock" file, maintain back-compat."""
        return f":{self}"


class LayerGroupIdentifier(str):
    """A string corresponding with a single layer group/directory name.

    This is not expected to be globally unique, only locally within their parent group.
    For example, there may be two group _paths_:

        * Foo/January
        * Bar/January

    `Foo`, `Bar`, `January` are all LayerGroupIdentifiers, but `January` is not globally
    unique, only locally (i.e. there can't be two `January`s in `Foo`).

    TODO: Update other models to replace string layer group identifiers with lists of
    this class?
    TODO: Dedup methods
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, cls):
            raise TypeError(f"Must be explicitly initialized with {cls.__name__}()")
        m = layer_group_identifier_regex.fullmatch(str(v))
        if not m:
            raise ValueError(f'Invalid layer group identifier format "{v}"')

        return v

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"

    def __json__(self):
        """When exporting to JSON to create a "lock" file, maintain back-compat."""
        return str(self)


class RootGroupSettings(QgrBaseModel):
    """Settings specific to the root group."""

    order: Optional[list[LayerIdentifier | LayerGroupIdentifier]]
    """The order in which this group's contents will be shown.

    Subgroups are referenced by name, e.g. 'Basemaps', and layers are
    referenced by a colon followed by the layer ID, e.g. `:background`. If
    'order' is omitted, a default sorting algorithm is applied.
    """

    # Without this setting, Pydantic will try and convert LayerGroupIdentifiers into
    # LayerIdentifiers because they look compatible and LayerIdentifier is first in the
    # union. This is slower. This is less of an issue in Pydantic v2.
    # https://docs.pydantic.dev/1.10/usage/model_config/#smart-union
    class Config:
        smart_union = True


class LayerGroupSettings(RootGroupSettings):
    expand: bool = False
    """Whether the group is expanded or collapsed in the QGIS Layers Panel."""

    show: bool = False
    """Whether the group is shown or hidden in the QGIS Layers Panel."""


AnyGroupSettings = Union[RootGroupSettings, LayerGroupSettings]
