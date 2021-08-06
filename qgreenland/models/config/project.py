from typing import Dict

from pydantic import BaseModel, FilePath


class BoundingBox(BaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


class ConfigBoundariesInfo(BaseModel):
    fp: FilePath
    bbox: BoundingBox


# TODO: re-consider this...proof of concept for dynamic model generation.
# In this case, it probably is OK to just statically define the project
# boundaries ('data' and 'background'. Alternatively, in this case, perhaps it's
# best just to define `ConfiProjectBoundaries` as Dict[str,
# ConfigBoundariesInfo]. Processing would be fetching these data by key anyway?
class ConfigProject(BaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
