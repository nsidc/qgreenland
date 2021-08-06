from abc import ABC
from typing import Dict, List, Literal, Union

from pydantic import AnyUrl, BaseModel, Field


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
    type: Literal['http']
    urls: List[AnyUrl]


class ConfigDatasetCmrAsset(ConfigDatasetAsset):
    type: Literal['cmr']
    granule_ur: str = Field(..., min_length=1)
    collection_concept_id: str = Field(..., min_length=1)


# It is unclear why we cannot just use `bound=ConfigDatasetAsset`, but suspect
# that pydantic does not try to find all subclasses of `ConfigDatasetAsset` when
# casting data to an appropriate model. Explicitly listing out the possible
# types allows pydantic to select the correct model based on the input data.
AnyAsset = Union[ConfigDatasetHttpAsset, ConfigDatasetCmrAsset]

# ... ogr_remote_vector, manual assets


class ConfigDataset(BaseModel):
    id: str = Field(..., min_length=1)
    assets: Dict[str, AnyAsset]
    metadata: ConfigDatasetMetadata
