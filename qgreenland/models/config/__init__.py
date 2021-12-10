from typing import Any

import anytree

from qgreenland.models.base_model import QgrBaseModel
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer
from qgreenland.models.config.project import Project


class Config(QgrBaseModel):
    """The configuration determines the pipeline outputs.

    All fields are populated programmatically. There is no need to specify a
    `Config` object anywhere: this is part of the framework.
    """

    project: Project
    """General project-wide configuration, such as CRS."""

    layers: dict[str, Layer]
    """A lookup of all layers included in the project."""

    datasets: dict[str, Dataset]
    """A lookup of all datasets included in the project."""

    layer_tree: anytree.Node
    """A tree of all layers and groups.

    Structured as they would be in the QGIS Layers Panel.
    """

    def __json__(self) -> dict[Any, Any]:
        return self.dict(
            include={'project', 'datasets', 'layer_tree'},
        )
