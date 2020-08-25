import os
from enum import Enum

from qgreenland import __version__

PROJECT = 'qgreenland'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT_DIR = '/input'
DATA_DIR = '/luigi/data'
RELEASES_DIR = os.path.join(DATA_DIR, 'release')
WIP_DIR = os.path.join(DATA_DIR, 'luigi-wip')
ASSETS_DIR = os.path.join(PACKAGE_DIR, 'assets')
LOCALDATA_DIR = os.path.join(ASSETS_DIR, 'local_data')
if 'dev' in __version__:
    RELEASE_DIR = os.path.join(RELEASES_DIR, 'dev', __version__)
else:
    RELEASE_DIR = os.path.join(RELEASES_DIR, __version__)

CONFIG_DIR = os.path.join(PACKAGE_DIR, 'config')
CONFIG_SCHEMA_DIR = os.path.join(CONFIG_DIR, 'schema')

# TMP_DIR is the same as WIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = WIP_DIR

# Output target file of the task just before the ZipQGreenland task.
# Presence indicates the project is ready to be zipped for release.
ZIP_TRIGGERFILE = os.path.join(WIP_DIR, 'READY_TO_ZIP')

REQUEST_TIMEOUT = 20

# URS stuff
URS_COOKIE = 'urs_user_already_logged'


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = INPUT_DIR

    # For still-processing data in temporary directory structure.
    WIP = os.path.join(WIP_DIR, 'wip')

    # For processed QGreenland data in its final directory structure.
    FINAL = os.path.join(WIP_DIR, f'{PROJECT}')
