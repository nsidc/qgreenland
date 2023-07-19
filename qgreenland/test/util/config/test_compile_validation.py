import pytest

# TODO: Write tests which exercise the compile_cfg function against directories
# with validation errors, ensuring that the correct errors are raised.
import qgreenland.exceptions as exc
from qgreenland.test.constants import (
    TEST_CONFIG_W_DUPES_DIR,
    TEST_CONFIG_W_EXTRA_SETTINGS_DIR,
    TEST_CONFIG_W_MISSING_SETTINGS_DIR,
    TEST_CONFIG_W_STRING_ORDER_VALUES,
)
from qgreenland.util.config.compile import compile_cfg


@pytest.mark.parametrize(
    "config,match_",
    [
        (
            TEST_CONFIG_W_MISSING_SETTINGS_DIR,
            "Found the following items on disk but not in ordered set",
        ),
        (TEST_CONFIG_W_EXTRA_SETTINGS_DIR, "Expected to find layer id"),
        (TEST_CONFIG_W_DUPES_DIR, "Duplicate layer_ids found"),
        (TEST_CONFIG_W_STRING_ORDER_VALUES, "Must be explicitly initialized"),
    ],
)
def test_failing_config(config, match_):
    with pytest.raises(exc.QgrConfigCompileError, match=match_):
        compile_cfg(config)
