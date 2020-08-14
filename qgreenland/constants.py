import os
from enum import Enum

from qgreenland import __version__
from qgreenland.util.config import make_config

PROJECT = 'qgreenland'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = '/luigi/data'
RELEASES_DIR = f'{DATA_DIR}/release'
WIP_DIR = f'{DATA_DIR}/luigi-wip'
ASSETS_DIR = f'{PACKAGE_DIR}/assets'
if 'dev' in __version__:
    RELEASE_DIR = f'{RELEASES_DIR}/dev/{__version__}'
else:
    RELEASE_DIR = f'{RELEASES_DIR}/{__version__}'

CONFIG_DIR = f'{PACKAGE_DIR}/config'
CONFIG_SCHEMA_DIR = f'{CONFIG_DIR}/schema'
CONFIG = make_config(config_dir=CONFIG_DIR, schema_dir=CONFIG_SCHEMA_DIR)

# TMP_DIR is the same as WIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = WIP_DIR

# Output target file of the task just before the ZipQGreenland task.
# Presence indicates the project is ready to be zipped for release.
ZIP_TRIGGERFILE = os.path.join(WIP_DIR, 'READY_TO_ZIP')

REQUEST_TIMEOUT = 20

# Project configuration
# NOTE: The order of this dictionary is important for passing to
# qgc.QgsRectangle
PROJECT_EXTENT = {'xmin': -3850000.000,
                  'ymin': -5350000.0,
                  'xmax': 3750000.0,
                  'ymax': 5850000.000}

PROJECT_CRS = 'EPSG:3413'

# URS stuff
URS_COOKIE = 'urs_user_already_logged'


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = os.path.join(WIP_DIR, 'fetch')

    # For still-processing data in temporary directory structure.
    WIP = os.path.join(WIP_DIR, 'wip')

    # For processed QGreenland data in its final directory structure.
    FINAL = os.path.join(WIP_DIR, f'{PROJECT}')
