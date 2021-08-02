from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class ConfigBoundariesInfo(BaseModel):
    fp: str
    # TODO: create class for features? (keys: type, id, propperties, geometry
    features: List[Dict[Any, Any]]
    bbox: Tuple[float, float, float, float]


class ConfigProjectBoundaries(BaseModel):
    background: ConfigBoundariesInfo
    data: ConfigBoundariesInfo


class ConfigProject(BaseModel):
    crs: str
    boundaries: ConfigProjectBoundaries
