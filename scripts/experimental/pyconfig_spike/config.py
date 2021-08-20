from scripts.experimental.pyconfig_spike.datasets.natural_earth import background as background_dataset
from scripts.experimental.pyconfig_spike.layers.background import background
from scripts.experimental.pyconfig_spike.project import project

from qgreenland.models.config import Config

CONFIG = Config(
    project=project,
    layers={'background': background},
    datasets={'background': background_dataset},
    hierarchy_settings=[],
)
