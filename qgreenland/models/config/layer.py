from typing import List, Optional

from pydantic import BaseModel, Field

from qgreenland.models.config.dataset import AnyAsset, ConfigDataset
from qgreenland.models.config.step import ConfigLayerStep


class ConfigLayerInput(BaseModel):
    # TODO: just maintain ids here?
    dataset: ConfigDataset
    asset: AnyAsset


class ConfigLayer(BaseModel):
    id: str

    # The layer name in QGIS layers panel:
    title: str

    # Descriptive text:
    description: str = Field(..., min_length=1)

    hierarchy: List[str]
    # in_package: bool

    # Is this layer initially "checked" as visible in QGIS?:
    show: bool = False

    # Which style (.qml) file to use for this layer?
    style: Optional[str] = Field(None, min_length=1)

    input: ConfigLayerInput

    steps: List[ConfigLayerStep]
