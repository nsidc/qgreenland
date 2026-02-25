from functools import cached_property
from pathlib import Path
from typing import Any, Optional, Union, cast

from pydantic import Field, validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.asset import OnlineAsset
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
    """A dataset's input to a layer's processing pipeline."""

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

    tags: list[str] = []
    """Additional categories that describe this data."""

    in_package: bool = True
    """Is this layer in the final QGreenland zip file?"""

    show: bool = False
    """Is this layer initially "checked" or visible in QGIS?"""

    style: Optional[str] = Field(None, min_length=1)
    """Which style (.qml) file to use for this layer?

    Omit the file extension.
    """

    inputs: list[LayerInput]

    steps: Optional[list[AnyStep]]

    @validator("inputs")
    @classmethod
    def ensure_inputs_online_asset(cls, value):
        """Ensure that, if an OnlineAsset input exists, that it is the only one."""
        if any(type(input) is OnlineAsset for input in value) and len(value) > 1:
            raise ValueError(
                "When an OnlineAsset is specified for a layer input"
                " it must be the only asset."
                " OnlineAsset is only used for online-only layers."
            )

        return value

    @cached_property
    def is_online_only(self):
        return len(self.inputs) == 1 and type(self.inputs[0].asset) is OnlineAsset

    @cached_property
    def online_only_asset(self) -> OnlineAsset | None:
        if self.is_online_only:
            asset = self.inputs[0].asset
            asset = cast(OnlineAsset, asset)
            return asset
        return None

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
                **{k: ... for k in self.dict().keys() if k != "inputs"},
                # TODO: inputs should probably be a list...?
                # "inputs": {
                #     "dataset": {"id"},
                #     "asset": {"id"},
                # },
            },
            exclude={
                "steps": {"__all__": {"id"}},
            },
        )
