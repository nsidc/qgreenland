import os
from enum import Enum
from pathlib import Path
from typing import Dict

from qgreenland._typing import (
    QgsLayerProviderType,
    QgsLayerType,
)
from qgreenland.util.version import (
    get_build_version,
    version_is_full_release,
)

PROJECT = 'QGreenland'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

PACKAGE_DIR = Path(__file__).parent
PROJECT_DIR = PACKAGE_DIR.parent
INPUT_DIR = Path('/input')
DATA_DIR = Path('/luigi/data')
PRIVATE_ARCHIVE_DIR = Path('/private-archive')
RELEASES_DIR = DATA_DIR / 'release'
WIP_DIR = DATA_DIR / 'luigi-wip'
ANCILLARY_DIR = PACKAGE_DIR / 'ancillary'
ASSETS_DIR = PACKAGE_DIR / 'assets'
TEST_DIR = PACKAGE_DIR / 'test'
SCRIPTS_DIR = PROJECT_DIR / 'scripts'

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
if version_is_full_release(version := get_build_version()):
    RELEASE_DIR = RELEASES_DIR / version
else:
    RELEASE_DIR = RELEASES_DIR / 'dev' / version

CONFIG_DIR = PACKAGE_DIR / 'config'
CONFIG_SCHEMA_DIR = CONFIG_DIR / 'schema'

# TMP_DIR is the same as WIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = WIP_DIR

# Output target file of the task just before the ZipQGreenland task.
# Presence indicates the project is ready to be zipped for release.
ZIP_TRIGGERFILE = WIP_DIR / 'READY_TO_ZIP'

REQUEST_TIMEOUT = 20

# URS stuff
URS_COOKIE = 'urs_user_already_logged'

PROVIDER_LAYERTYPE_MAPPING: Dict[QgsLayerProviderType, QgsLayerType] = {
    'gdal': 'Raster',
    'wms': 'Raster',
    'wfs': 'Vector',
}


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = INPUT_DIR

    # For still-processing data in temporary directory structure.
    WIP = WIP_DIR / 'wip'

    # For processed QGreenland data in its final directory structure.
    FINAL = WIP_DIR / f'{PROJECT}'
