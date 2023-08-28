from pathlib import Path
from typing import Any, Optional, Union

from pydantic import Field

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import AnyAsset, Dataset
from qgreenland.models.config.step import AnyStep
from qgreenland.util.layer_style import get_style_filepath
from qgreenland.util.model_validators import reusable_validator, validate_paragraph_text
from qgreenland.util.model_validators.layer_style import (
    validate_style_file_continuous_legend,
    validate_style_file_exists,
    validate_style_file_only_contains_allowed_fonts,
)


class LayerInput(QgrBaseModel):
    """The input(s) to a layer's processing pipeline."""

    # TODO: just maintain ids here?
    dataset: Dataset
    """The dataset providing the layer's input. Important for metadata."""

    asset: AnyAsset
    """The actual input asset (file or files)."""


class Layer(QgrBaseModel):
    id: str
    """Unique identifier."""

    title: str
    """The layer name in QGIS Layers Panel."""

    description: str = Field(..., min_length=1)
    """Descriptive text shown as hover-text in the QGIS Layer Panel."""

    # Temporary keeping these around for testing before config is fully migrated
    in_package: bool = True
    tags: list[str] = []

    packaging_tags: list[str] = ["core"]
    """Which packages does this layer belong in? Layer will be omitted if empty.

    Temporarily defaults to ["core"] to help us test more quickly.

    TODO: Validate len > 0.
    """

    show: bool = False
    """Is this layer initially "checked" or visible in QGIS?"""

    style: Optional[str] = Field(None, min_length=1)
    """Which style (.qml) file to use for this layer?

    Omit the file extension.
    """

    input: LayerInput

    steps: Optional[list[AnyStep]]

    _validate_description = reusable_validator("description", validate_paragraph_text)
    _validate_style_file_exists = reusable_validator(
        "style",
        validate_style_file_exists,
    )
    _validate_style_file_only_contains_allowed_fonts = reusable_validator(
        "style",
        validate_style_file_only_contains_allowed_fonts,
    )
    _validate_style_file_continuous_legend = reusable_validator(
        "style",
        validate_style_file_continuous_legend,
    )

    @property
    def style_filepath(self) -> Union[Path, None]:
        """Full filepath to the QML style file."""
        if self.style is None:
            return None

        return get_style_filepath(self.style)

    def __json__(self) -> dict[Any, Any]:
        """Limit child models that are output when dumping JSON.

        When dumping a layer tree, we shouldn't include all the datasets and the
        assets because that results in severe duplication.
        """
        return self.dict(
            include={
                **{k: ... for k in self.dict().keys() if k != "input"},
                "input": {
                    "dataset": {"id"},
                    "asset": {"id"},
                },
            },
            exclude={
                "steps": {"__all__": {"id"}},
            },
        )
