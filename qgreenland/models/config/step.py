from typing import List

from pydantic import BaseModel

from qgreenland._typing import ConfigStepType


class ConfigLayerStep(BaseModel):
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
