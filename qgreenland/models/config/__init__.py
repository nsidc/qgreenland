from typing import Any

import anytree

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer
from qgreenland.models.config.project import Project


class Config(QgrBaseModel):
    project: Project
    layers: dict[str, Layer]
    datasets: dict[str, Dataset]
    layer_tree: anytree.Node

    def __json__(self) -> dict[Any, Any]:
        return self.dict(
            include={'project', 'datasets', 'layer_tree'},
        )
