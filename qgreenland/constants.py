import os
from pathlib import Path

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

# TODO: Rename to FETCH_DIR? FETCHED_DIR? THE_FETCH_SPOT? FETCHY_MC_FETCH_FACE?
# Something else?
INPUT_DIR = Path('/input')

DATA_DIR = Path('/luigi/data')
PRIVATE_ARCHIVE_DIR = Path('/private-archive')

# TODO: Separate the layer hosting location from the package hosting location
RELEASES_DIR = DATA_DIR / 'release'
RELEASES_LAYERS_DIR = RELEASES_DIR / 'layers'

LUIGIWIP_DIR = DATA_DIR / 'luigi-wip'
WIP_DIR = LUIGIWIP_DIR / 'wip'
PACKAGE_COMPILE_DIR = LUIGIWIP_DIR / PROJECT
ANCILLARY_DIR = PACKAGE_DIR / 'ancillary'
TEMPLATES_DIR = ANCILLARY_DIR / 'templates'
ASSETS_DIR = PACKAGE_DIR / 'assets'
SCRIPTS_DIR = PROJECT_DIR / 'scripts'

# TODO: INPUT_DIR as an "output location" doesn't sound right.
OUTPUT_DIRS = (
    INPUT_DIR,
    WIP_DIR,
    RELEASES_LAYERS_DIR,
    PACKAGE_COMPILE_DIR,
)

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
if version_is_full_release(version := get_build_version()):
    RELEASE_DIR = RELEASES_DIR / version
else:
    RELEASE_DIR = RELEASES_DIR / 'dev' / version

CONFIG_DIR = PACKAGE_DIR / 'config'
LAYERS_CFG_DIR = CONFIG_DIR / 'layers'

# TMP_DIR is the same as LUIGIWIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = LUIGIWIP_DIR

# In seconds. See
# https://2.python-requests.org/en/master/user/quickstart/#timeouts
REQUEST_TIMEOUT = 30

# URS stuff
URS_COOKIE = 'urs_user_already_logged'

PROVIDER_LAYERTYPE_MAPPING: dict[QgsLayerProviderType, QgsLayerType] = {
    'gdal': 'Raster',
    'wms': 'Raster',
    'wfs': 'Vector',
}
