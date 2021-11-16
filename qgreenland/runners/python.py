from qgreenland.models.config.step import LayerStep


def python_runner(
    step: LayerStep,
    *,
    input_dir: str,
    output_dir: str,
) -> None:
    ...
