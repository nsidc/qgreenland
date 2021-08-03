from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.util.config import make_config

from qgreenland.models.config.hierarchy import HierarchySettings
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.step_template import ConfigStepTemplate
from qgreenland.models.config import Config

init_conf = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

CONFIG = Config(
    project=init_conf['project'],
    layers=init_conf['layers'],
    datasets=[ConfigDataset(**dataset) for dataset in init_conf['datasets']],
    step_templates=[ConfigStepTemplate(name=name, **step_template) for name, step_template in init_conf['step_templates'].items()],
    hierarchy_settings=[HierarchySettings(path=path, **settings) for path, settings in init_conf['hierarchy_settings'].items()]
)
