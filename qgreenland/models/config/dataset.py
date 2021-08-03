from typing import Any, Dict, List

from pydantic import BaseModel, validator


class ConfigDatasetCitation(BaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(BaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDataset(BaseModel):
    id: str
    assets: List[Dict[str, Any]]
    metadata: ConfigDatasetMetadata

    # TODO: re-consider this approach...
    @validator('assets')
    def deref_assets(cls, value, values, **kwargs):
        if not value:
            # TOOD: better err and qgr exception
            raise RuntimeError('PROBLEM!!!!')

        assets = {}
        for asset in value:
            assets[asset['id']] = asset

        return assets


