from pathlib import Path
from typing import Optional

from qgreenland.models.config.asset import DatasetAsset
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import AnyStep
from qgreenland.util.layer import (
    get_layer_path_by_id,
    get_vrt_ref_data_relpath,
)


def write_provenance_file(*, layer_cfg: Layer, filepath: Path) -> None:
    """Write layer provenance to a text file."""
    txt_to_write = layer_provenance_text(layer_cfg)

    with open(filepath, "w") as provenance_file:
        provenance_file.write(
            txt_to_write,
        )


def layer_provenance_text(layer_cfg: Layer) -> str:
    # TODO: default message for layers with no processing steps? Just include a
    # string that indicates where the data were fetched from?
    provenance_text = ""
    if referenced_layer_id := layer_cfg.vrt_layer_ref_id:
        reference_layer_relfp = get_vrt_ref_data_relpath(layer_cfg)
        reference_layer_path = get_layer_path_by_id(referenced_layer_id)
        provenance_text = (
            f"# Data for this layer are read from {reference_layer_relfp}.\n"
            f'# See the "{reference_layer_path}" layer metadata for more information.'
        )
    elif layer_cfg.steps:
        for layer_input in layer_cfg.inputs:
            assert isinstance(layer_input, LayerInput)
            provenance_text += _asset_provenance_text(layer_input.asset)
            steps_provenance = _steps_provenance_text(layer_cfg.steps)
            if steps_provenance:
                provenance_text += "\n\n# Data processed using the following steps:\n\n"
                provenance_text += steps_provenance

    return provenance_text


def _steps_provenance_text(steps: Optional[list[AnyStep]]) -> Optional[str]:
    if not steps:
        return None

    steps_as_text = [step.provenance for step in steps]

    return "\n\n".join(steps_as_text)


def _asset_provenance_text(asset: DatasetAsset) -> str:
    return asset.provenance
