from typing import Dict

from pydantic import FilePath

from qgreenland.models.base_model import QgrBaseModel


class BoundingBox(QgrBaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


class ConfigBoundariesInfo(QgrBaseModel):
    fp: FilePath
    bbox: BoundingBox


class ConfigProject(QgrBaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]
