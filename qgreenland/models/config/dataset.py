from abc import ABC
from typing import Dict, List, Literal, Union

from pydantic import AnyUrl, Field

from qgreenland._typing import QgsLayerProviderType
from qgreenland.models.base_model import QgrBaseModel


class ConfigDatasetCitation(QgrBaseModel):
    text: str
    url: str


class ConfigDatasetMetadata(QgrBaseModel):
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetAsset(QgrBaseModel, ABC):
    id: str = Field(..., min_length=1)


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[AnyUrl]


# TODO: OnlineRaster/OnlineVector asset types? The thing that makes this a
# "gdal_remote" layer is the `/vsicurl/` prefix. Otherwise, this is created as a
# regular layer with a URL as its path.
class ConfigDatasetOnlineAsset(ConfigDatasetAsset):
    provider: QgsLayerProviderType
    # AnyUrl alone doesn't work because "gdal" remote layers use a
    # `/vsicurl/https://` prefix, "wms" remote layers prefix the URL with
    # parameters. Maybe "url" isn't a good name for this parameter.
    url: Union[AnyUrl, str] = Field(..., min_length=1)


class ConfigDatasetCmrAsset(ConfigDatasetAsset):
    granule_ur: str = Field(..., min_length=1)
    collection_concept_id: str = Field(..., min_length=1)


class ConfigDatasetManualAsset(ConfigDatasetAsset):
    type: Literal['manual'] = 'manual'
    access_instructions: str = Field(..., min_length=1)


# TODO: local assets
AnyAsset = Union[
    ConfigDatasetHttpAsset,
    ConfigDatasetOnlineAsset,
    ConfigDatasetCmrAsset,
    ConfigDatasetManualAsset,
]


class ConfigDataset(QgrBaseModel):
    id: str = Field(..., min_length=1)
    assets: Dict[str, AnyAsset]
    metadata: ConfigDatasetMetadata
