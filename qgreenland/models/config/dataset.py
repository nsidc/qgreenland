from pydantic import Field, validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.asset import AnyAsset
from qgreenland.util.model_validators import reusable_validator, validate_paragraph_text


class DatasetCitation(QgrBaseModel):
    """Citation for a dataset."""

    text: str
    """The citation text."""

    url: str
    """The citation URL. This is usually a doi.org URL."""

    @validator('text')
    @classmethod
    def strip_enclosing_newlines(cls, value):
        """Clean up the citation text."""
        return value.lstrip('\n').rstrip('\n')


class DatasetMetadata(QgrBaseModel):
    """Metadata for the dataset."""

    title: str
    """The dataset's title. Please use sentence case, not title case."""

    abstract: str
    """The dataset abstract."""
    citation: DatasetCitation

    _abstract_validator = reusable_validator('abstract', validate_paragraph_text)


class Dataset(QgrBaseModel):
    """Configuration for a dataset."""

    id: str = Field(..., min_length=1)
    """Dataset unique identifier."""

    assets: dict[str, AnyAsset]
    """Actual data associated with the dataset."""

    metadata: DatasetMetadata

    @validator('assets', pre=True)
    @classmethod
    def index_assets_by_id(cls, value):
        """Reindex assets from a list to a dictionary keyed by `id`."""
        if type(value) != list:
            raise TypeError(f'Expected list, received: {value}')

        ids = [asset.id for asset in value]
        if len(set(ids)) != len(ids):
            raise TypeError(f'Duplicate id found in: {value}')

        return {asset.id: asset for asset in value}
