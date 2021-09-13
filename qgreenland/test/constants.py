from enum import Enum

from qgreenland.constants import PACKAGE_DIR


TEST_DIR = PACKAGE_DIR / 'test'
TEST_DATA_DIR = TEST_DIR / 'data'
TEST_CONFIG_DIR = TEST_DATA_DIR / 'config'
TEST_CONFIG_W_DUPES_DIR = TEST_DATA_DIR / 'config_with_duplicates'
MOCK_LAYERS_DIR = PACKAGE_DIR / 'test' / 'data' / 'layers'


class MockTaskType(Enum):
    FINAL = str(MOCK_LAYERS_DIR)
