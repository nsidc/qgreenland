from typing import Dict

from pydantic import Field, validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.asset import AnyAsset


class ConfigDatasetCitation(QgrBaseModel):
    text: str
    url: str

    @validator('text')
    @classmethod
    def strip_enclosing_newlines(cls, value):
        return value.lstrip('\n').rstrip('\n')


class ConfigDatasetMetadata(QgrBaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDataset(QgrBaseModel):
    id: str = Field(..., min_length=1)
    assets: Dict[str, AnyAsset]
    metadata: ConfigDatasetMetadata

    @validator('assets', pre=True)
    @classmethod
    def index_assets_by_id(cls, value):
        if type(value) != list:
            raise TypeError(f'Expected list, received: {value}')

        ids = [asset.id for asset in value]
        if len(set(ids)) != len(ids):
            raise TypeError(f'Duplicate id found in: {value}')

        return {asset.id: asset for asset in value}
