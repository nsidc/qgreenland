from typing import Generic, List

from pydantic import BaseModel

from qgreenland.models.config.dataset import AnyAsset, ConfigDataset
from qgreenland.models.config.step import ConfigLayerStep


class ConfigLayerInput(BaseModel, Generic[AnyAsset]):
    # TODO: just maintain ids here?
    dataset: ConfigDataset
    asset: AnyAsset


class ConfigLayer(BaseModel):
    id: str

    # The layer name in QGIS layers panel:
    title: str

    # Descriptive text:
    description: str = ''

    hierarchy: List[str]
    # in_package: bool

    # Is this layer initially "checked" as visible in QGIS?:
    show: bool = False

    # Which style (.qml) file to use for this layer?
    # TODO: require? Better default?
    style: str = ''

    input: ConfigLayerInput

    steps: List[ConfigLayerStep]

    # TODO: remove.
    # This was for overriding the output projection of a layer.
    project_crs: str = ''
