from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.util.config import make_config

CONFIG = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import create_project_config_model

layer = CONFIG['layers']['background']
layer_conf = ConfigLayer(**layer)
project = CONFIG['project']
project_conf = create_project_config_model(project)
breakpoint()
