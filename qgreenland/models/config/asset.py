from abc import ABC, abstractmethod
from functools import cached_property
from typing import Union

from pydantic import AnyUrl, Field, validator

import qgreenland.exceptions as exc
from qgreenland._typing import QgsLayerProviderType
from qgreenland.constants.paths import ASSETS_DIR
from qgreenland.models.base_model import QgrBaseModel
from qgreenland.util.runtime_vars import EvalFilePath, EvalStr


class DatasetAsset(QgrBaseModel, ABC):
    id: str = Field(..., min_length=1)

    @abstractmethod
    def provenance(self) -> str:
        pass


class HttpAsset(DatasetAsset):
    # Whether or not to verify server's TLS certificate.
    #     https://2.python-requests.org/en/master/api/#requests.Session.request
    verify_tls: bool = True

    urls: list[AnyUrl]

    @cached_property
    def provenance(self) -> str:
        return f'Data fetched via HTTP from {self.urls}'


# TODO: OnlineRaster/OnlineVector asset types? The thing that makes this a
# "gdal_remote" layer is the `/vsicurl/` prefix. Otherwise, this is created as a
# regular layer with a URL as its path.
class OnlineAsset(DatasetAsset):
    provider: QgsLayerProviderType
    # AnyUrl alone doesn't work because "gdal" remote layers use a
    # `/vsicurl/https://` prefix, "wms" remote layers prefix the URL with
    # parameters. Maybe "url" isn't a good name for this parameter.
    url: Union[AnyUrl, str] = Field(..., min_length=1)

    @cached_property
    def provenance(self) -> str:
        return (
            f'Data accessed online with QGIS Layer Provider {self.provider} at'
            f'url {self.url}'
        )


class CmrAsset(DatasetAsset):
    granule_ur: str = Field(..., min_length=1)
    collection_concept_id: str = Field(..., min_length=1)

    @cached_property
    def provenance(self) -> str:
        return (
            f'Data discovered via CMR with granule UR {self.granule_ur} and'
            f' collection concept ID {self.collection_concept_id}'
        )


class RepositoryAsset(DatasetAsset):
    """Assets stored in this repository in `ASSETS_DIR`."""

    # TODO: Move the assets into the config directory???
    filepath: EvalFilePath

    @validator('filepath')
    @classmethod
    def ensure_relative_to_assets(cls, value):
        evaluated = value.eval()
        try:
            evaluated.relative_to(ASSETS_DIR)
        except Exception as e:
            raise exc.QgrInvalidConfigError(
                f'Expected path relative to {{assets_dir}}.'
                f' Received: {evaluated}. ({e})',
            )

        return value

    @cached_property
    def provenance(self) -> str:
        return f'Data accessed in QGreenland repository at {self.filepath}'


class ManualAsset(DatasetAsset):
    """Assets that must be manually accessed by a human.

    e.g., requires interactive login.
    """

    access_instructions: str = Field(..., min_length=1)

    @cached_property
    def provenance(self) -> str:
        return (
            'Data accessed manually by a human following instructions:\n'
            f'{self.access_instructions}'
        )


class CommandAsset(DatasetAsset):
    """Assets that are fetched via an arbitrary command.

    Data is written to '{output_dir}', which _must_ be specified in the command.
    """

    args: list[EvalStr]

    @cached_property
    def provenance(self) -> str:
        return f'Data accessed using command:\n{self.args}'


AnyAsset = Union[
    CmrAsset,
    CommandAsset,
    HttpAsset,
    ManualAsset,
    OnlineAsset,
    RepositoryAsset,
]
