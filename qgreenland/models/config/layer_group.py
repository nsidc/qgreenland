from typing import Optional, Union

from qgreenland.models.base_model import QgrBaseModel


class RootGroupSettings(QgrBaseModel):
    """Settings specific to the root group."""

    order: Optional[list[str]]
    """The order in which this group's contents will be shown.

    Subgroups are referenced by name, e.g. 'Basemaps', and layers are
    referenced by a colon followed by the layer ID, e.g. `:background`. If
    'order' is omitted, a default sorting algorithm is applied.
    """


class LayerGroupSettings(RootGroupSettings):
    expand: bool = False
    """Whether the group is expanded or collapsed in the QGIS Layers Panel."""

    show: bool = False
    """Whether the group is shown or hidden in the QGIS Layers Panel."""


AnyGroupSettings = Union[RootGroupSettings, LayerGroupSettings]
