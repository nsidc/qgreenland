from abc import ABC
from typing import Any, List

from pydantic import AnyUrl, BaseModel, Field, validator


class ConfigDatasetCitation(BaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(BaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetAsset(BaseModel, ABC):
    id: str = Field(..., min_length=1)


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[AnyUrl]


class ConfigDatasetCmrAsset(ConfigDatasetAsset):
    granule_ur: str = Field(..., min_length=1)
    collection_concept_id: str = Field(..., min_length=1)


# ... ogr_remote_vector, manual assets


class ConfigDataset(BaseModel):
    id: str = Field(..., min_length=1)
    assets: List[ConfigDatasetAsset] = Field(..., min_items=1)
    metadata: ConfigDatasetMetadata

    # TODO: Better type than List[Any]?
    @classmethod
    @validator('assets')
    def handle_asset_subtypes(cls, value: List[Any]) -> List[Any]:
        """."""
        assets = []
        mapping = {
            'http': ConfigDatasetHttpAsset,
        }
        for asset in value:
            if asset.type in mapping.keys():
                assets.append(mapping[asset.type](**asset))
            else:
                raise RuntimeError(
                    f'Only {mapping.keys()} assets are currently supported.'
                )

        # breakpoint()
        return assets
