from typing import Any, List

from pydantic import AnyUrl, BaseModel, validator


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


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[AnyUrl]


class ConfigDataset(BaseModel):
    id: str
    assets: List[ConfigDatasetAsset]
    metadata: ConfigDatasetMetadata

    # TODO: Better type than List[Any]?
    @classmethod
    @validator('assets')
    def check_assets_not_empty(cls, value: List[Any]) -> None:
        if not value:
            raise RuntimeError('Expected a list of assets.')

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
