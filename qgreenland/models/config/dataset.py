from typing import Any, List

from pydantic import AnyUrl, BaseModel, Field, validator


class ConfigDatasetCitation(BaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(BaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetAsset(BaseModel):
    id: str = Field(..., min_length=1)

    # Allow extra attrs for http, cmr, etc.
    # TODO: better way to handle this. Maybe with TypeVar and Generic?
    class Config:
        extra = 'allow'


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[AnyUrl]


class ConfigDataset(BaseModel):
    id: str = Field(..., min_length=1)
    assets: List[ConfigDatasetAsset] = Field(..., min_items=1)
    metadata: ConfigDatasetMetadata

    # TODO: Better type than List[Any]?
    @classmethod
    @validator('assets')
    def handle_asset_subtypes(cls, value: List[Any]) -> List[Any]:
        assets = []
        for asset in value:
            if 'http' in asset.dict():
                assets.append(ConfigDatasetHttpAsset(id=asset.id, **asset.http))
            else:
                # TODO
                raise RuntimeError('Only http assets are currently supported!!!')

        return assets
