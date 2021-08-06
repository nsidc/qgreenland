from typing import List

from qgreenland._typing import ConfigStepType
from qgreenland.models.immutable_model import ImmutableBaseModel


class ConfigLayerStep(ImmutableBaseModel):
    type: ConfigStepType

    # input_file: Path
    # output_file: Path
    args: List[str]

    # If template:
    # template_name: str
    # kwargs: Dict[str, Any]

    # If command:
    # args: List[str, int]

    # If Python:
    # kwargs: Dict[str, Any]
