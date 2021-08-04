from typing import Dict, List

from pydantic import BaseModel

from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.hierarchy import HierarchySettings
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import ConfigProject


class Config(BaseModel):
    project: ConfigProject
    layers: Dict[str, ConfigLayer]
    datasets: Dict[str, ConfigDataset]
    hierarchy_settings: List[HierarchySettings]
