from pathlib import Path

import pytest

from qgreenland.constants import ASSETS_DIR
from qgreenland.exceptions import QgrInterpolationError
from qgreenland.models.config.step import ConfigLayerCommandStep
from qgreenland.util.runtime_vars import EvalFilePath, EvalPath, EvalStr


def test_eval_path():
    eval_path = EvalPath('{assets_dir}/arctic_circle.geojson')
    expected = ASSETS_DIR / 'arctic_circle.geojson'

    assert eval_path.eval() == expected

    # Assert eval w/ kwarg works as expected.
    input_dir = '/foo/bar'
    expected = Path(f'{input_dir}/baz.tif')
    assert EvalPath('{input_dir}/baz.tif').eval(input_dir=input_dir) == expected

    # Assert eval w/ unexpected kwarg
    with pytest.raises(TypeError):
        EvalPath('{foo}/baz.tif').eval(foo='bar')


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

    # concatenation
    assert isinstance(EvalStr('{input_dir}/') + 'foobar.txt', EvalStr)


def test_config_layer_cmd_step_args_validation():
    command_step = ConfigLayerCommandStep(
        args=[
            'foo',
            'bar',
            'baz',
        ],
    )

    assert all(isinstance(arg, EvalStr) for arg in command_step.args)
