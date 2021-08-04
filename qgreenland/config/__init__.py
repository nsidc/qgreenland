from qgreenland.constants import CONFIG_DIR, CONFIG_SCHEMA_DIR
from qgreenland.models.config import Config
from qgreenland.models.config.dataset import ConfigDataset
from qgreenland.models.config.hierarchy import HierarchySettings
from qgreenland.util.config import make_config


# TODO: Consider doing dereferencing in pydantic validators
init_conf = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

CONFIG = Config(
    project=init_conf['project'],
    layers=init_conf['layers'],
    datasets={
        dataset['id']: ConfigDataset(**dataset) for dataset in init_conf['datasets']
    },
    hierarchy_settings=[
        HierarchySettings(
            path=path,
            **settings
        ) for path, settings in init_conf['hierarchy_settings'].items()
    ]
)
