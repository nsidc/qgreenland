import os
from enum import Enum

from qgreenland.util.version import get_build_version, version_is_full_release

PROJECT = 'QGreenland'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(PACKAGE_DIR, os.pardir))
INPUT_DIR = '/input'
DATA_DIR = '/luigi/data'
PRIVATE_ARCHIVE_DIR = '/private-archive'
RELEASES_DIR = os.path.join(DATA_DIR, 'release')
WIP_DIR = os.path.join(DATA_DIR, 'luigi-wip')
ASSETS_DIR = os.path.join(PACKAGE_DIR, 'assets')
LOCALDATA_DIR = os.path.join(ASSETS_DIR, 'local_data')
TEST_DIR = os.path.join(PACKAGE_DIR, 'test')

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
if version_is_full_release(version := get_build_version()):
    RELEASE_DIR = os.path.join(RELEASES_DIR, version)
else:
    RELEASE_DIR = os.path.join(RELEASES_DIR, 'dev', version)

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
