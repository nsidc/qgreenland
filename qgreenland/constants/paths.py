from pathlib import Path

from qgreenland.constants.project import PROJECT
from qgreenland.util.version import (
    get_build_version,
    version_is_full_release,
)


PACKAGE_DIR = Path(__file__).parent.parent
PROJECT_DIR = PACKAGE_DIR.parent

CONFIG_DIR = PACKAGE_DIR / 'config'
LAYERS_CFG_DIR = CONFIG_DIR / 'layers'

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
    # RELEASES_DIR,
    RELEASES_LAYERS_DIR,
    PACKAGE_COMPILE_DIR,
)

# TMP_DIR is the same as LUIGIWIP_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = LUIGIWIP_DIR

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
if version_is_full_release(version := get_build_version()):
    RELEASE_DIR = RELEASES_DIR / version
else:
    RELEASE_DIR = RELEASES_DIR / 'dev' / version
