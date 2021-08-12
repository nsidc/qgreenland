from functools import cached_property
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

    # @cache
    # def _provenance_text(self) -> str:
    #     return 'foo'

    # TODO: ABC for COnfigLayerStep, subclasses for command, python func.
    @cached_property
    def provenance(self) -> str:
        return ' '.join(self.args)
