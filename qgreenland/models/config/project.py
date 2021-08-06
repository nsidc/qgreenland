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


class ConfigProject(BaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
