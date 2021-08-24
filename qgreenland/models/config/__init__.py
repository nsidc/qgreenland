from typing import Dict, List

import anytree
from pydantic import BaseModel

from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.hierarchy import HierarchySettings
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import ConfigProject


class Config(BaseModel):
    """Validated and de-referenced configuration."""

    project: ConfigProject
    layers: Dict[str, ConfigLayer]
    datasets: Dict[str, ConfigDataset]
    layer_tree: anytree.Node

    class Config:
        arbitrary_types_allowed = True
