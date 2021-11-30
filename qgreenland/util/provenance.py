from pathlib import Path

from qgreenland.models.config.asset import DatasetAsset
from qgreenland.models.config.layer import Layer
from qgreenland.models.config.step import AnyStep


def write_provenance_file(*, layer_cfg: Layer, filepath: Path) -> None:
    """Write layer provenance to a text file."""
    # TODO: default message for layers with no processing steps? Just include a
    # string that indicates where the data were fetched from?
    txt_to_write = ''

    if layer_cfg.steps:
        txt_to_write = layer_provenance_text(layer_cfg)

    with open(filepath, 'w') as provenance_file:
        provenance_file.write(
            txt_to_write,
        )


def layer_provenance_text(layer_cfg: Layer) -> str:
    fetch_provenance = _asset_provenance_text(layer_cfg.input.asset)
    steps_provenance = _steps_provenance_text(layer_cfg.steps)

    return fetch_provenance + '\n\n' + steps_provenance


def _steps_provenance_text(steps: list[AnyStep]) -> str:
    steps_as_text = [step.provenance for step in steps]

    return '\n\n'.join(steps_as_text)


def _asset_provenance_text(asset: DatasetAsset) -> str:
    return asset.provenance
