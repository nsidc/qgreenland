from typing import Any, Dict, List

from pydantic import BaseModel

from qgreenland.models.config.step import ConfigLayerStep
from qgreenland.models.config.dataset import ConfigDatasetMetadata


class ConfigLayerInput(BaseModel):
    # TODO: De-reference?
    # Reference
    dataset: str
    # Reference
    asset: str


class ConfigLayerDataset(BaseModel):
    id: str
    metadata: ConfigDatasetMetadata
    asset: Dict[str, Any]


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
    # TODO: deref
    dataset: ConfigLayerDataset

    steps: List[ConfigLayerStep]

    # TODO: remove.
    # This was for overriding the output projection of a layer.
    project_crs: str = ''
