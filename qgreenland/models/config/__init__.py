from typing import Any

import anytree

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import ConfigProject


class Config(QgrBaseModel):
    project: ConfigProject
    layers: dict[str, ConfigLayer]
    datasets: dict[str, ConfigDataset]
    layer_tree: anytree.Node

    def __json__(self) -> dict[Any, Any]:
        return self.dict(
            include={'project', 'datasets', 'layer_tree'},
        )
