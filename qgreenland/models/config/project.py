from typing import Any, Dict, List, Tuple

from pydantic import create_model, BaseModel


class ConfigBoundariesInfo(BaseModel):
    fp: str
    # TODO: create class for features? (keys: type, id, propperties, geometry
    features: List[Dict[Any, Any]]
    bbox: Tuple[float, float, float, float]



# TODO: re-consider this...proof of concept for dynamic model generation.
# In this case, it probably is OK to just statically define the project
# boundaries ('data' and 'background'. Alternatively, in this case, perhaps it's
# best just to define `ConfiProjectBoundaries` as Dict[str,
# ConfigBoundariesInfo]. Processing would be fetching these data by key anyway?
class ConfigProject(BaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
