from typing import List

from pydantic import BaseModel

from qgreenland.models.config.step import ConfigLayerStep


class ConfigLayerInput(BaseModel):
    # TODO: De-reference?
    # Reference
    dataset: str
    # Reference
    asset: str


class ConfigLayer(BaseModel):
    id: str

    # The layer name in QGIS layers panel:
    title: str

    # Descriptive text:
    # TODO: require? Better default?
    description: str = ''

    hierarchy: List[str]
    # in_package: bool


    # Is this layer initially "checked" as visible in QGIS?:
    show: bool

    # Which style (.qml) file to use for this layer?
    # TODO: require? Better default?
    style: str = ''
    
    input: ConfigLayerInput

    steps: List[ConfigLayerStep]


