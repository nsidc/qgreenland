import pytest

from qgreenland.models.config.step import PythonStep


def _mock_processing_func(*, input_dir: str, output_dir: str):
    print(input_dir)
    print(output_dir)


def test_python_step_provenance():
    py_step = PythonStep(function=_mock_processing_func)

    # The module path for the mock processing func defined in this file resolves
    # to the current module name (`test_step`)
    assert "Python Step: test_step:_mock_processing_func" in py_step.provenance


def test_python_step_raises_err_bad_func_sig():
    def _mock_bad_processing_func(only_one_arg_not_expected: bool):
        print(only_one_arg_not_expected)

    with pytest.raises(ValueError, match="Expected the provided PythonStep"):
        PythonStep(function=_mock_bad_processing_func)
