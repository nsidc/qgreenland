from abc import ABC
from pathlib import Path
from typing import Dict, List, Union

from pydantic import AnyUrl, Field, validator

from qgreenland._typing import QgsLayerProviderType
from qgreenland.models.base_model import QgrBaseModel


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

    @validator('abstract')
    @classmethod
    def strip_enclosing_newlines(cls, value):
        return value.lstrip('\n').rstrip('\n')


class ConfigDatasetAsset(QgrBaseModel, ABC):
    id: str = Field(..., min_length=1)


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    # Whether or not to verify server's TLS certificate.
    #     https://2.python-requests.org/en/master/api/#requests.Session.request
    verify_tls: bool = True

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


class ConfigDatasetRepositoryAsset(ConfigDatasetAsset):
    """Assets stored in this repository in `ASSETS_DIR`."""

    # TODO: Move the assets into the config directory???
    # TODO: Full path or relative path to ASSETS_DIR?
    filepath: Path


class ConfigDatasetManualAsset(ConfigDatasetAsset):
    """Assets that must be manually accessed by a human.

    e.g., requires interactive login.
    """

    access_instructions: str = Field(..., min_length=1)


# TODO: local assets
AnyAsset = Union[
    ConfigDatasetHttpAsset,
    ConfigDatasetOnlineAsset,
    ConfigDatasetCmrAsset,
    ConfigDatasetRepositoryAsset,
    ConfigDatasetManualAsset,
]


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
