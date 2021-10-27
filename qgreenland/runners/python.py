from qgreenland.models.config.step import ConfigLayerStep


def python_runner(
    step: ConfigLayerStep,
    *,
    input_dir: str,
    output_dir: str,
) -> None:
    ...
