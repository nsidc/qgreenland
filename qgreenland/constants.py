import os
from enum import Enum
from pathlib import Path

from qgreenland.util.version import (
    get_build_version,
    version_is_full_release,
)
from qgreenland._typing import (
    QgsLayerProviderType,
    QgsLayerType,
)

PROJECT = 'QGreenland'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = Path(__file__).parent
PROJECT_DIR = PACKAGE_DIR.parent
INPUT_DIR = '/input'
DATA_DIR = '/luigi/data'
PRIVATE_ARCHIVE_DIR = '/private-archive'
RELEASES_DIR = os.path.join(DATA_DIR, 'release')
WIP_DIR = os.path.join(DATA_DIR, 'luigi-wip')
ASSETS_DIR = os.path.join(PACKAGE_DIR, 'assets')
LOCALDATA_DIR = os.path.join(ASSETS_DIR, 'local_data')
TEST_DIR = os.path.join(PACKAGE_DIR, 'test')
SCRIPTS_DIR = os.path.join(PROJECT_DIR, 'scripts')

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
if version_is_full_release(version := get_build_version()):
    RELEASE_DIR = os.path.join(RELEASES_DIR, version)
else:
    RELEASE_DIR = os.path.join(RELEASES_DIR, 'dev', version)

CONFIG_DIR = PACKAGE_DIR / 'config'
CONFIG_SCHEMA_DIR = CONFIG_DIR / 'schema'

# TMP_DIR is the same as WIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = WIP_DIR

# Output target file of the task just before the ZipQGreenland task.
# Presence indicates the project is ready to be zipped for release.
ZIP_TRIGGERFILE = os.path.join(WIP_DIR, 'READY_TO_ZIP')

REQUEST_TIMEOUT = 20

# URS stuff
URS_COOKIE = 'urs_user_already_logged'

PROVIDER_LAYERTYPE_MAPPING: Dict[QgsLayerProviderType, QgsLayerType] = {
    'gdal': 'Raster',
    'wms': 'Raster',
}


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = INPUT_DIR

    # For still-processing data in temporary directory structure.
    WIP = os.path.join(WIP_DIR, 'wip')

    # For processed QGreenland data in its final directory structure.
    FINAL = os.path.join(WIP_DIR, f'{PROJECT}')
