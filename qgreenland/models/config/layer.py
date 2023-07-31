from pathlib import Path
from typing import Any, Optional, Union
from xml.etree import ElementTree

from pydantic import Field, validator

import qgreenland.exceptions as exc
from qgreenland.constants.paths import ANCILLARY_DIR
from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import AnyAsset, Dataset
from qgreenland.models.config.step import AnyStep
from qgreenland.util.model_validators import reusable_validator, validate_paragraph_text


class LayerInput(QgrBaseModel):
    """The input(s) to a layer's processing pipeline."""

    # TODO: just maintain ids here?
    dataset: Dataset
    """The dataset providing the layer's input. Important for metadata."""

    asset: AnyAsset
    """The actual input asset (file or files)."""


def _style_filepath(style_name: str) -> Path:
    return ANCILLARY_DIR / "styles" / (style_name + ".qml")


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

    input: LayerInput

    steps: Optional[list[AnyStep]]

    _validate_description = reusable_validator("description", validate_paragraph_text)

    @validator("style")
    @classmethod
    def style_file_only_contains_allowed_fonts(cls, value):
        """Ensure only fonts that can be downloaded by QGIS are in our style files.

        This ensures we don't re-trigger an old issue:
            https://github.com/nsidc/qgreenland/issues/515
        """
        # TODO: Is the full list of supported fonts available in PyQGIS' API? I think
        # this is the complete list, but haven't found it in the Python API yet:
        #     https://github.com/qgis/QGIS/blob/a7b31c7db29328fc44966a854d22c452f58c77c1/src/core/textrenderer/qgsfontmanager.cpp#L203-L925
        allowed_fonts = ["Open Sans"]
        if value:
            style_filepath = _style_filepath(value)
            tree = ElementTree.parse(style_filepath)
            for elem in tree.getroot().iter():
                if font_family := elem.attrib.get("fontFamily", False):
                    if font_family not in allowed_fonts:
                        raise exc.QgrInvalidConfigError(
                            f"Style {style_filepath} contains disallowed font:"
                            f" '{font_family}'."
                            f" Only the following fonts are allowed: {allowed_fonts}."
                        )

        return value

    @validator("style")
    @classmethod
    def style_file_exists(cls, value):
        """Ensure the QML style file exists in the configuration."""
        if value:
            style_filepath = _style_filepath(value)
            if not style_filepath.is_file():
                raise exc.QgrInvalidConfigError(
                    f"Style file does not exist: {style_filepath}"
                )

        return value

    @property
    def style_filepath(self) -> Union[Path, None]:
        """Full filepath to the QML style file."""
        if self.style is None:
            return None

        return _style_filepath(self.style)

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
