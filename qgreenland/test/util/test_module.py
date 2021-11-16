import pytest

from qgreenland.models.config.layer import Layer
from qgreenland.test.constants import (
    TEST_CONFIG_DIR,
    TEST_DATA_DIR,
)
from qgreenland.util.module import (
    load_objects_from_paths_by_class,
    module_from_path,
)


sample_module = TEST_CONFIG_DIR / 'layers' / 'Group' / 'Subgroup' / 'examples.py'
sample_module_w_error = TEST_DATA_DIR / 'sample_module_zerodiv.py'


def test_module_from_path_nofile_raises():
    with pytest.raises(FileNotFoundError):
        module_from_path(TEST_DATA_DIR / 'foo.py')


def test_module_from_path_error_raises():
    with pytest.raises(ZeroDivisionError):
        module_from_path(sample_module_w_error)


def test_load_objects_from_paths_by_class():
    objs = load_objects_from_paths_by_class(
        [sample_module],
        target_class=Layer,
    )
    for obj in objs:
        assert type(obj) is Layer
