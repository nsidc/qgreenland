from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.util.config import make_config

CONFIG = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import ConfigProject

layer = CONFIG['layers']['background']
# breakpoint()
layer_conf = ConfigLayer(**layer)
project = CONFIG['project']
project_conf = ConfigProject(**project)
breakpoint()
