from abc import ABC
from pathlib import Path
from typing import List, Union

from pydantic import AnyUrl, Field, validator

from qgreenland._typing import QgsLayerProviderType
from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalStr


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
    # String representing path with `{assets_dir}` slug so the config can be
    # diffed across systems.
    filepath: EvalStr

    @validator('filepath')
    @classmethod
    def ensure_relative_to_assets(cls, value):
        interpolated_value = value.eval()
        if not Path(interpolated_value).is_file():
            raise ValueError(f'No file found at {interpolated_value}.')

        return value


class ConfigDatasetManualAsset(ConfigDatasetAsset):
    """Assets that must be manually accessed by a human.

    e.g., requires interactive login.
    """

    access_instructions: str = Field(..., min_length=1)


AnyAsset = Union[
    ConfigDatasetCmrAsset,
    ConfigDatasetHttpAsset,
    ConfigDatasetManualAsset,
    ConfigDatasetOnlineAsset,
    ConfigDatasetRepositoryAsset,
]
