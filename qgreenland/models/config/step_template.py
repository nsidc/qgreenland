from typing import List

from pydantic import BaseModel


class ConfigStep(BaseModel):
    type: str
    args: List[str]


class ConfigStepTemplate(BaseModel):
    name: str
    kwargs: List[str]
    steps: List[ConfigStep]
