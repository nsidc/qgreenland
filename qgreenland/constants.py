import os
from enum import Enum

import yamale

from qgreenland import __version__

PROJECT = 'qgreenland'


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = '/luigi/data'
RELEASES_DIR = f'{DATA_DIR}/release'
WIP_DIR = f'{DATA_DIR}/luigi-wip'
ASSETS_DIR = f'{PACKAGE_DIR}/assets'
CONFIG_DIR = f'{PACKAGE_DIR}/config'
CONFIG_SCHEMA_DIR = f'{CONFIG_DIR}/schema'

if 'dev' in __version__:
    RELEASE_DIR = f'{RELEASES_DIR}/dev/{__version__}'
else:
    RELEASE_DIR = f'{RELEASES_DIR}/{__version__}'

# TMP_DIR is the same as WIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = WIP_DIR

# Output target file of the task just before the ZipQGreenland task.
# Presence indicates the project is ready to be zipped for release.
ZIP_TRIGGERFILE = os.path.join(WIP_DIR, 'READY_TO_ZIP')

REQUEST_TIMEOUT = 3

# Project configuration
# NOTE: The order of this dictionary is important for passing to qgc.QgsRectangle
BBOX = {'xmin': -3850000.000, 'ymin': -5350000.0, 'xmax': 3750000.0, 'ymax': 5850000.000}
BBOX_POLYGON = [
    (BBOX['xmin'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymax']),
]
PROJECT_CRS = 'EPSG:3411'

# URS stuff
URS_COOKIE = 'urs_user_already_logged'


def _load_config(config_filename):
    """Validate config file against schema with Yamale.

    It is expected that the given config filename in CONFIG_DIR has a schema of
    matching name in CONFIG_SCHEMA_DIR.

    Yamale can read in directories of config files, so it returns a list of
    (data, fp) tuples. We always read single files, so we return just the data
    from result[0][0].
    """
    config_fp = os.path.join(CONFIG_DIR, config_filename)
    schema_fp = os.path.join(CONFIG_SCHEMA_DIR, config_filename)

    if not os.path.isfile(config_fp):
        return NotImplementedError(
            'Loading is supported for only one config file at a time.'
        )

    schema = yamale.make_schema(schema_fp)
    config = yamale.make_data(config_fp)
    yamale.validate(schema, config)

    return config[0][0]


CONFIG = {
    'layers': _load_config('layers.yml'),
    'layer_groups': _load_config('layer_groups.yml')
}


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = os.path.join(WIP_DIR, 'fetch')

    # For still-processing data in temporary directory structure.
    WIP = os.path.join(WIP_DIR, 'wip')

    # For processed QGreenland data in its final directory structure.
    FINAL = os.path.join(WIP_DIR, f'{PROJECT}')
