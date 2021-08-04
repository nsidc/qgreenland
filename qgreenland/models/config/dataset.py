from typing import List

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

    @validator('assets')
    def validate_assets(cls, value):  # noqa:N805
        # `value` is a list of assets.
        if not value:
            # TODO: better.
            raise RuntimeError('Very problem.')

        assets = []
        for asset in value:
            if 'http' in asset.dict():
                assets.append(ConfigDatasetHttpAsset(id=asset.id, **asset.http))
            else:
                # TODO
                raise RuntimeError('Only http assets are currently supported!!!')

        return assets
