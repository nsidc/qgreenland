from pathlib import Path

from qgreenland.constants.project import PROJECT
from qgreenland.util.version import get_build_version, version_is_full_release

PACKAGE_DIR = Path(__file__).parent.parent
PROJECT_DIR = PACKAGE_DIR.parent

CONFIG_DIR = PACKAGE_DIR / "config"
LAYERS_CFG_DIR = CONFIG_DIR / "layers"

PRIVATE_ARCHIVE_DIR = Path("/private-archive")

WORKING_STORAGE_DIR = Path("/working-storage")
FETCH_DATASETS_DIR = WORKING_STORAGE_DIR / "fetch-datasets"

WIP_LAYERS_DIR = WORKING_STORAGE_DIR / "wip-layers"
WIP_PACKAGE_DIR = WORKING_STORAGE_DIR / "wip-package"

RELEASE_LAYERS_DIR = WORKING_STORAGE_DIR / "release-layers"
RELEASE_PACKAGES_DIR = WORKING_STORAGE_DIR / "release-packages"

COMPILE_PACKAGE_DIR = WIP_PACKAGE_DIR / PROJECT

ANCILLARY_DIR = PACKAGE_DIR / "ancillary"
TEMPLATES_DIR = ANCILLARY_DIR / "templates"
ASSETS_DIR = PACKAGE_DIR / "assets"
SCRIPTS_DIR = PROJECT_DIR / "scripts"

INTERMEDIATE_DIRS = (
    FETCH_DATASETS_DIR,
    WIP_LAYERS_DIR,
    WIP_PACKAGE_DIR,
)

# TODO: Extract to function in another module to remove constants dependency on
# get_build_version, version_is_full_release
PACKAGE_VERSION = get_build_version()
if version_is_full_release(PACKAGE_VERSION):
    VERSIONED_PACKAGE_DIR = RELEASE_PACKAGES_DIR / PACKAGE_VERSION
else:
    VERSIONED_PACKAGE_DIR = RELEASE_PACKAGES_DIR / "dev" / PACKAGE_VERSION
