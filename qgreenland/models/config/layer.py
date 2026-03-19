from functools import cached_property
from pathlib import Path
from typing import Any, Optional, TypeGuard, Union, cast

from pydantic import Field, validator

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.asset import ManualAsset, OnlineAsset
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
    """A dataset input to a layer's processing pipeline."""

    # TODO: just maintain ids here?
    dataset: Dataset
    """The dataset providing the layer's input. Important for metadata."""

    asset: AnyAsset
    """The actual input asset (file or files)."""


class VectorLayerReferenceInput(QgrBaseModel):
    """Layer input that references another vector layer's finalized output via a VRT.

    Note that the author of layers using `VectorLayerReferenceInput` must
    validate the end result manually.
    """

    layer_id: str
    """The referenced layer's ID."""

    sql: str
    """SQL statement that selects data from the referenced layer."""


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

    inputs: list[LayerInput | VectorLayerReferenceInput]

    steps: Optional[list[AnyStep]]

    @validator("inputs")
    @classmethod
    def ensure_inputs(cls, value):
        """Ensure that inputs with unique expectations match those expectations.

        * If an input exists with an OnlineAsset asset, it must be the only one.
        * If a VectorLayerReferenceInput input exists, it must be the only one.
        """
        inputs = value

        # Currently, both cases expect only 1 input. If the number of inputs for
        # a layer is 1, then this check passes.
        if len(inputs) <= 1:
            return inputs

        # Online layers are identfied by the presence of a single LayerInput
        # with it's `asset` of type OnlineAsset.
        if any(
            type(lyr_input.asset) is OnlineAsset
            for lyr_input in inputs
            if type(lyr_input) is LayerInput
        ):
            raise ValueError(
                "When an OnlineAsset is used for a layer input"
                " it must be the only asset."
                " OnlineAsset is only used for online-only layers."
            )
        elif any(type(lyr_input) is VectorLayerReferenceInput for lyr_input in inputs):
            raise ValueError(
                "When a VectorLayerReferenceInput is used for a layer input"
                " it must be the only input."
            )

        return inputs

    @staticmethod
    def _is_online_only(
        inputs: list[LayerInput | VectorLayerReferenceInput],
    ) -> TypeGuard[list[LayerInput]]:
        """Typegaurd OnlineOnly layers having only LayerInput."""
        return (
            len(inputs) == 1
            and isinstance(inputs[0], LayerInput)
            and type(inputs[0].asset) is OnlineAsset
        )

    @cached_property
    def is_online_only(self):
        return self._is_online_only(self.inputs)

    @staticmethod
    def _is_vrt_layer(
        inputs: list[LayerInput | VectorLayerReferenceInput],
    ) -> TypeGuard[list[VectorLayerReferenceInput]]:
        """Typegaurd VRT layers having only VectorLayerReferenceInput."""
        return len(inputs) == 1 and isinstance(inputs[0], VectorLayerReferenceInput)

    @cached_property
    def is_vrt_layer(self):
        return self._is_vrt_layer(self.inputs)

    @cached_property
    def vrt_layer_ref_id(self) -> str | None:
        """If this is a VRT layer, return the referenced data's ID."""
        if not self._is_vrt_layer(self.inputs):
            return None

        return self.inputs[0].layer_id

    @cached_property
    def includes_manual_asset(self):
        return (
            isinstance(self.inputs[0], LayerInput)
            and type(self.inputs[0].asset) is ManualAsset
        )

    @cached_property
    def online_only_asset(self) -> OnlineAsset | None:
        if self._is_online_only(self.inputs):
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
                "inputs": {
                    "__all__": {
                        "dataset": {"id"},
                        "asset": {"id"},
                    },
                },
            },
            exclude={
                "steps": {"__all__": {"id"}},
            },
        )
