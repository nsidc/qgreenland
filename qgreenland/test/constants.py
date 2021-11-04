from qgreenland.constants import PACKAGE_DIR


TEST_DIR = PACKAGE_DIR / 'test'
TEST_DATA_DIR = TEST_DIR / 'data'
TEST_CONFIG_DIR = TEST_DATA_DIR / 'config'

# TODO: Why doesn't the "with_duplicates" dir have any tests against it?
TEST_CONFIG_W_DUPES_DIR = TEST_DATA_DIR / 'config_with_duplicates'

TEST_CONFIG_W_EXTRA_SETTINGS_DIR = TEST_DATA_DIR / 'config_with_extra_settings'
TEST_CONFIG_W_MISSING_SETTINGS_DIR = TEST_DATA_DIR / 'config_with_missing_settings'
MOCK_PACKAGE_COMPILE_DIR = TEST_DATA_DIR / 'compile'
MOCK_RELEASES_LAYERS_DIR = TEST_DATA_DIR / 'release' / 'layers'
