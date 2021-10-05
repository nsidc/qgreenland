import pytest

from qgreenland.constants import ASSETS_DIR
from qgreenland.exceptions import QgrInterpolationError
from qgreenland.util.runtime_vars import EvalFilePath, EvalPath, EvalStr


def test_eval_path():
    eval_path = EvalPath('{assets_dir}/arctic_circle.geojson')
    expected = ASSETS_DIR / 'arctic_circle.geojson'

    assert eval_path.eval() == expected


def test_eval_file_path():
    eval_path = EvalFilePath('{assets_dir}/arctic_circle.geojson')
    expected = ASSETS_DIR / 'arctic_circle.geojson'

    assert eval_path.eval() == expected

    with pytest.raises(QgrInterpolationError):
        EvalFilePath('{assets_dir}/DEFINITELY_DOES_NOT_EXIST.FOOBAR').eval()


def test_eval_str():
    eval_str = EvalStr('{assets_dir} is very cool')
    expected = f'{ASSETS_DIR} is very cool'

    assert eval_str.eval() == expected
