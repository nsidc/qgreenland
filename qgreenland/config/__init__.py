from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.util.config import make_config

CONFIG = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.project import create_project_config_model
from qgreenland.models.config.hierarchy import HierarchySettings
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.step_template import ConfigStepTemplate

layer = CONFIG['layers']['background']
layer_conf = ConfigLayer(**layer)
project = CONFIG['project']
project_conf = create_project_config_model(project)
hierarchy = CONFIG['hierarchy_settings']
hierarchy_conf = [HierarchySettings(path=path, **settings) for path, settings in hierarchy.items()]
datasets = CONFIG['datasets']
dataset_conf = [ConfigDataset(**dataset) for dataset in datasets]
step_templates = CONFIG['step_templates']  # Dict[str, Dict]
step_templates_conf = [ConfigStepTemplate(name=name, **step_template) for name, step_template in step_templates.items()]
breakpoint()
