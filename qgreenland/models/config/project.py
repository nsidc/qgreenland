from typing import Dict

from pydantic import FilePath

from qgreenland.models.immutable_model import ImmutableBaseModel


class BoundingBox(ImmutableBaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


class ConfigBoundariesInfo(ImmutableBaseModel):
    fp: FilePath
    bbox: BoundingBox


class ConfigProject(ImmutableBaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
