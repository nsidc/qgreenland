import datetime as dt
from pathlib import Path

from qgreenland.constants.paths import FETCH_DATASETS_DIR
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.util.layer import (
    datasource_dirname,
    get_layer_cfg_for_id,
    get_layer_path_by_id,
)


def build_layer_metadata(layer_cfg: Layer) -> str:
    """Return layer metadata text.

    Includes layer description, dataset description, and citation information.
    """
    # Include the layer description first.
    abstract = build_layer_description(layer_cfg)

    if referenced_layer_id := layer_cfg.vrt_layer_ref_id:
        layer_inputs = get_layer_cfg_for_id(referenced_layer_id).inputs
        abstract += "\n\n=== Note! ===\n"
        reference_layer_path = get_layer_path_by_id(referenced_layer_id)
        abstract += f'Data for this layer are derived from "{reference_layer_path}"\n'
        abstract += "See that layer's metadata for more information."
    else:
        layer_inputs = layer_cfg.inputs

    original_data_sources = []
    dataset_ids = []
    for layer_input in layer_inputs:
        assert isinstance(layer_input, LayerInput)
        # Create only one original data source per unique input dataset.
        dataset_id = layer_input.dataset.id
        if dataset_id in dataset_ids:
            continue
        dataset_ids.append(dataset_id)

        original_data_source = ""
        original_data_source += _build_dataset_description(layer_input.dataset)

        if original_data_source:
            original_data_source += "\n\n"

        # Add the dataset's citation
        original_data_source += _build_dataset_citation(layer_input)
        original_data_source += "\n-------------------------------\n"
        original_data_sources.append(original_data_source)

    # If the layer has a description, separate it from the abstract of the
    # original data source.
    if abstract:
        abstract += "\n\n=== Original Data Source(s) ===\n"

    abstract += "".join(original_data_sources)

    return abstract


def write_metadata_file(*, layer_cfg: Layer, filepath: Path) -> None:
    """Write layer metadata to a text file."""
    with open(filepath, "w") as metadata_file:
        metadata_file.write(
            build_layer_metadata(layer_cfg),
        )


def build_layer_description(layer_cfg: Layer) -> str:
    """Return a string representing the layer's description."""
    layer_description = ""

    if cfg_description := layer_cfg.description:
        layer_description += cfg_description

    return layer_description


def _build_dataset_description(dataset: Dataset) -> str:
    """Return a string representing the layer's dataset description.

    Description includes dataset title and abstract.
    """
    dataset_metadata = dataset.metadata
    dataset_description = f"Title:\n{dataset_metadata.title}"

    if abstract := dataset_metadata.abstract:
        dataset_description += "\n\n"
        dataset_description += f"Abstract:\n{abstract}"

    return dataset_description


# TODO: this could take a dataset cfg instead of a layer_cfg and be
# cached. Sometimes multiple layers are derived from the same dataset.
def _build_dataset_citation(layer_input: LayerInput) -> str:
    """Return a string representing the layer's dataset citation."""
    citation = ""

    dataset_metadata = layer_input.dataset.metadata
    if citation_cfg := dataset_metadata.citation:
        if citation_text := citation_cfg.text:
            ct = _populate_date_accessed(citation_text, layer_input=layer_input)
            citation += "Citation:\n"
            citation += ct + "\n\n"

        if citation_url := citation_cfg.url:
            citation += "Citation URL:\n"
            citation += citation_url

    return citation


def _populate_date_accessed(text: str, *, layer_input: LayerInput) -> str:
    if "{{date_accessed}}" not in text:
        return text

    ds_dir = datasource_dirname(
        dataset_id=layer_input.dataset.id,
        asset_id=layer_input.asset.id,
    )
    fetch_dir = Path(FETCH_DATASETS_DIR) / ds_dir

    # TODO: Use modified time for directory, or latest modified time for files
    # inside?
    mtime = fetch_dir.stat().st_mtime
    date_accessed = dt.datetime.utcfromtimestamp(mtime)

    date_accessed_str = f"[Accessed on: {date_accessed.date().isoformat()}]"
    return text.replace("{{date_accessed}}", date_accessed_str)
