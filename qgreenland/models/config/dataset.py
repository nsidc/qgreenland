from typing import Any, Dict, List

from pydantic import BaseModel, validator


class ConfigDatasetCitation(BaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(BaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetAsset(BaseModel):
    id: str

    # Allow extra attrs for http, cmr, etc.
    # TODO: better way to handle this. Maybe with TypeVar and Generic?
    class Config:
        extra = 'allow'


class ConfigDataset(BaseModel):
    id: str
    assets: List[ConfigDatasetAsset]
    metadata: ConfigDatasetMetadata
