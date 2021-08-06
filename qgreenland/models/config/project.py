from typing import Any, Dict, List

from pydantic import BaseModel


class BoundingBox(BaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


class ConfigBoundariesInfo(BaseModel):
    fp: str
    # TODO: create class for features? (keys: type, id, propperties, geometry
    features: List[Dict[Any, Any]]
    bbox: BoundingBox


# TODO: re-consider this...proof of concept for dynamic model generation.
# In this case, it probably is OK to just statically define the project
# boundaries ('data' and 'background'. Alternatively, in this case, perhaps it's
# best just to define `ConfiProjectBoundaries` as Dict[str,
# ConfigBoundariesInfo]. Processing would be fetching these data by key anyway?
class ConfigProject(BaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
