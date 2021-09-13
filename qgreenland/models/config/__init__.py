from typing import Dict

import anytree

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import ConfigProject


class Config(QgrBaseModel):
    project: ConfigProject
    layers: Dict[str, ConfigLayer]
    datasets: Dict[str, ConfigDataset]
    layer_tree: anytree.Node
