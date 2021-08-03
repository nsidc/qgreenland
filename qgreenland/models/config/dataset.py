from typing import Any, Dict, List

from pydantic import BaseModel, validator


class ConfigDatasetAsset(BaseModel):
    id: str
    verify: bool = True


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[str]


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

        assets = []
        for asset in value:
            if 'http' in asset.keys():
                assets.append(ConfigDatasetHttpAsset(id=asset['id'], **asset['http']))
            else:
                # TODO: better err
                raise RuntimeError('Unsupported asset configuration.')

        return assets


