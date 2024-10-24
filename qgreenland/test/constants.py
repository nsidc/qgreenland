from qgreenland.constants.paths import PACKAGE_DIR

TEST_DIR = PACKAGE_DIR / "test"
TEST_DATA_DIR = TEST_DIR / "data"
TEST_CONFIG_DIR = TEST_DATA_DIR / "config"

TEST_CONFIG_W_DUPES_DIR = TEST_DATA_DIR / "config_with_duplicates"
TEST_CONFIG_W_EXTRA_SETTINGS_DIR = TEST_DATA_DIR / "config_with_extra_settings"
TEST_CONFIG_W_MISSING_SETTINGS_DIR = TEST_DATA_DIR / "config_with_missing_settings"
TEST_CONFIG_W_STRING_ORDER_VALUES = TEST_DATA_DIR / "config_with_string_order_values"

# TODO: Handle new package-specific compile dirs
MOCK_COMPILE_PACKAGE_DIR = TEST_DATA_DIR / "compile"
MOCK_RELEASE_LAYERS_DIR = TEST_DATA_DIR / "release" / "layers"
