import inspect
from typing import Optional, Union

from qgreenland.models.base_model import QgrBaseModel


# TODO: We're currently breaking the convention of prefixing all config models
# with Config. Change?

class RootGroupSettings(QgrBaseModel):
    # The order in which this group's contents (including subgroups) will be
    # shown. Subgroups are referenced by name, e.g. 'Basemaps', and layers are
    # referenced by module and object name, e.g. 'background.py:background'. If
    # 'order' is omitted, a default sorting algorithm is applied.
    order: Optional[list[str]]



class LayerGroupSettings(RootGroupSettings):
    # Whether the group is expanded or collapsed in the QGIS Layers Panel
    expand: bool = False

    # Whether the group is shown (checked) or hidden (unchecked) in the QGIS
    # Layers Panel
    show: bool = False


AnyGroupSettings = Union[RootGroupSettings, LayerGroupSettings]
