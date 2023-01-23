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
    """Actual data associated with the dataset.

    Assets determine how this data is accessed.
    """

    id: str = Field(..., min_length=1)
    """Asset unique identifier. Must be unique within the dataset."""

    @abstractmethod
    @cached_property
    def provenance(self) -> str:
        """How the asset was acquired."""
        pass


class HttpAsset(DatasetAsset):
    """An asset fetched over HyperText Transfer Protocol."""

    verify_tls: bool = True
    """Verify the server's TLS certificate?

        https://2.python-requests.org/en/master/api/#requests.Session.request
    """

    urls: list[AnyUrl]
    """List of URLs to fetch."""

    @cached_property
    def provenance(self) -> str:
        return f"# Data fetched via HTTP from {[str(u) for u in self.urls]}"


# TODO: OnlineRaster/OnlineVector asset types? The thing that makes this a
# "gdal_remote" layer is the `/vsicurl/` prefix. Otherwise, this is created as a
# regular layer with a URL as its path.
class OnlineAsset(DatasetAsset):
    """A QGIS online layer that is not fetched, but is accessed by QGIS."""

    provider: QgsLayerProviderType
    """The Layer Provider to use when setting up this layer in QGIS."""

    # NOTE: AnyUrl alone doesn't work because "gdal" remote layers use a
    # `/vsicurl/https://` prefix, "wms" remote layers prefix the URL with
    # parameters. Maybe "url" isn't a good name for this parameter.
    url: Union[AnyUrl, str] = Field(..., min_length=1)
    """The URL to use when setting up this layer in QGIS."""

    @cached_property
    def provenance(self) -> str:
        return (
            f"# Data accessed online with QGIS Layer Provider {self.provider}"
            f" at url {self.url}"
        )


class CmrAsset(DatasetAsset):
    """Data fetched based on the location provided by CMR."""

    granule_ur: str = Field(..., min_length=1)
    """The CMR unique granule UR identifier."""

    collection_concept_id: str = Field(..., min_length=1)
    """The CMR unique collection concept identifier."""

    @cached_property
    def provenance(self) -> str:
        return (
            f"# Data discovered via CMR with granule UR {self.granule_ur} and"
            f" collection concept ID {self.collection_concept_id}"
        )


class RepositoryAsset(DatasetAsset):
    """Data stored in this repository in `ASSETS_DIR`."""

    # TODO: Move the assets into the config directory???
    filepath: EvalFilePath
    """The location of the asset, e.g. `{assets_dir}/foo.txt`."""  # noqa: FS003

    @validator("filepath")
    @classmethod
    def ensure_relative_to_assets(cls, value):
        """Ensure the asset path is as expected."""
        evaluated = value.eval()
        try:
            evaluated.relative_to(ASSETS_DIR)
        except Exception as e:
            raise exc.QgrInvalidConfigError(
                f"Expected path relative to {{assets_dir}}."
                f" Received: {evaluated}. ({e})",
            )

        return value

    @cached_property
    def provenance(self) -> str:
        return f"# Data accessed in QGreenland repository at {self.filepath}"


class ManualAsset(DatasetAsset):
    """Data that must be manually accessed by a human.

    For example, data which require an interactive login.
    """

    access_instructions: str = Field(..., min_length=1)
    """Instructions for accessing the asset."""

    @cached_property
    def provenance(self) -> str:
        return (
            "# Data accessed manually by a human following instructions:\n\n"
            f"{self.access_instructions}"
        )


class CommandAsset(DatasetAsset):
    """Data that are fetched via an arbitrary command.

    Data is written to '{output_dir}', which _must_ be specified in the command.
    """

    args: list[EvalStr]
    """Command arguments.

    E.g.: `['echo', 'foo', '>', '{output_dir}/foo.txt']`.
    """

    @cached_property
    def provenance(self) -> str:
        command = " ".join([str(arg) for arg in self.args])
        return f"# Data accessed using command:\n\n{command}"


AnyAsset = Union[
    CmrAsset,
    CommandAsset,
    HttpAsset,
    ManualAsset,
    OnlineAsset,
    RepositoryAsset,
]
