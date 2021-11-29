from pathlib import Path

from qgreenland.models.config.layer import Layer
from qgreenland.models.config.step import AnyStep


def steps_to_provenance_text(steps: list[AnyStep]) -> str:
    steps_as_text = [step.provenance for step in steps]

    return '\n\n'.join(steps_as_text)


def write_provenance_file(*, layer_cfg: Layer, filepath: Path) -> None:
    """Write layer provenance to a text file."""
    # TODO: default message for layers with no processing steps?
    txt_to_write = ''

    if layer_cfg.steps:
        txt_to_write = steps_to_provenance_text(layer_cfg.steps)

    with open(filepath, 'w') as provenance_file:
        provenance_file.write(
            txt_to_write,
        )
