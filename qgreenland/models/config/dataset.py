from abc import ABC
from typing import Dict, List, Literal, Union

from pydantic import AnyUrl, Field

from qgreenland.models.immutable_model import ImmutableBaseModel


class ConfigDatasetCitation(ImmutableBaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(ImmutableBaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetAsset(ImmutableBaseModel, ABC):
    id: str = Field(..., min_length=1)


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    type: Literal['http']
    urls: List[AnyUrl]


class ConfigDatasetGdalRemoteAsset(ConfigDatasetAsset):
    type: Literal['gdal_remote']
    # AnyUrl doesn't work because of `/vsicurl/https://` prefix
    url: str = Field(..., min_length=1)


class ConfigDatasetCmrAsset(ConfigDatasetAsset):
    type: Literal['cmr']
    granule_ur: str = Field(..., min_length=1)
    collection_concept_id: str = Field(..., min_length=1)


AnyAsset = Union[
    ConfigDatasetHttpAsset,
    ConfigDatasetGdalRemoteAsset,
    ConfigDatasetCmrAsset
]

# ... ogr_remote_vector, manual assets


class ConfigDataset(ImmutableBaseModel):
    id: str = Field(..., min_length=1)
    assets: Dict[str, AnyAsset]
    metadata: ConfigDatasetMetadata
