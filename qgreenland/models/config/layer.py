from typing import Any, Optional

from pydantic import Field

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import AnyAsset, ConfigDataset
from qgreenland.models.config.step import AnyStep
from qgreenland.models.validators import reusable_validator, validate_paragraph_text


class ConfigLayerInput(QgrBaseModel):
    # TODO: just maintain ids here?
    dataset: ConfigDataset
    asset: AnyAsset


class ConfigLayer(QgrBaseModel):
    id: str

    # The layer name in QGIS layers panel:
    title: str

    # Descriptive text:
    description: str = Field(..., min_length=1)

    # Additional categories that describe this data:
    tags: list[str] = []

    # Is this layer in the final QGreenland zip file?:
    in_package: bool = True

    # Is this layer initially "checked" as visible in QGIS?:
    show: bool = False

    # Which style (.qml) file to use for this layer?
    style: Optional[str] = Field(None, min_length=1)

    input: ConfigLayerInput

    steps: Optional[list[AnyStep]]

    _validate_description = reusable_validator('description', validate_paragraph_text)

    def __json__(self) -> dict[Any, Any]:
        """Limit child models that are output when dumping JSON.

        When dumping a layer tree, we shouldn't include all the datasets and the
        assets because that results in severe duplication.
        """
        return self.dict(
            include={
                **{k: ... for k in self.dict().keys() if k != 'input'},
                'input': {
                    'dataset': {'id'},
                    'asset': {'id'},
                },
            },
            exclude={
                'steps': {'__all__': {'id'}},
            },
        )
