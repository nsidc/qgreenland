from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.util.config import make_config

CONFIG = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

from qgreenland.models.config.layer import ConfigLayer

layer = CONFIG['layers']['background']
# breakpoint()
layer_conf = ConfigLayer(**layer)
breakpoint()
