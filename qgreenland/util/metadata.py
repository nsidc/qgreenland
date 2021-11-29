import datetime as dt
from pathlib import Path

from qgreenland.constants.paths import FETCH_DATASETS_DIR
from qgreenland.models.config.layer import Layer
from qgreenland.util.layer import datasource_dirname


def build_layer_metadata(layer_cfg: Layer) -> str:
    """Return layer metadata text.

    Includes layer description, dataset description, and citation information.
    """
    # Include the layer description first.
    abstract = build_layer_description(layer_cfg)

    # If the layer has a description, separate it from the abstract of the
    # original data source.
    if abstract:
        abstract += '\n\n=== Original Data Source ===\n'

    abstract += _build_dataset_description(layer_cfg)

    if abstract:
        abstract += '\n\n'

    # Add the dataset's citation
    abstract += _build_dataset_citation(layer_cfg)

    return abstract


def write_metadata_file(*, layer_cfg: Layer, filepath: Path) -> None:
    """Write layer metadata to a text file."""
    with open(filepath, 'w') as metadata_file:
        metadata_file.write(
            build_layer_metadata(layer_cfg),
        )


def build_layer_description(layer_cfg: Layer) -> str:
    """Return a string representing the layer's description."""
    layer_description = ''

    if cfg_description := layer_cfg.description:
        layer_description += cfg_description

    return layer_description


# TODO: this could take a dataset cfg instead of a layer_cfg and be
# cached. Sometimes multiple layers are derived from the same dataset.
def _build_dataset_description(layer_cfg: Layer) -> str:
    """Return a string representing the layer's dataset description.

    Description includes dataset title and abstract.
    """
    dataset_description = ''

    dataset_metadata = layer_cfg.input.dataset.metadata
    dataset_description += dataset_metadata.title

    if abstract := dataset_metadata.abstract:
        dataset_description += '\n\n'
        dataset_description += abstract

    return dataset_description


# TODO: this could take a dataset cfg instead of a layer_cfg and be
# cached. Sometimes multiple layers are derived from the same dataset.
def _build_dataset_citation(layer_cfg: Layer) -> str:
    """Return a string representing the layer's dataset citation."""
    citation = ''

    dataset_metadata = layer_cfg.input.dataset.metadata
    if citation_cfg := dataset_metadata.citation:
        if citation_text := citation_cfg.text:
            ct = _populate_date_accessed(citation_text, layer_cfg=layer_cfg)
            citation += 'Citation:\n'
            citation += ct + '\n\n'

        if citation_url := citation_cfg.url:
            citation += 'Citation URL:\n'
            citation += citation_url

    return citation


def _populate_date_accessed(text: str, *, layer_cfg: Layer) -> str:
    if '{{date_accessed}}' not in text:
        return text

    ds_dir = datasource_dirname(
        dataset_id=layer_cfg.input.dataset.id,
        asset_id=layer_cfg.input.asset.id,
    )
    fetch_dir = Path(FETCH_DATASETS_DIR) / ds_dir

    # TODO: Use modified time for directory, or latest modified time for files
    # inside?
    mtime = fetch_dir.stat().st_mtime
    date_accessed = dt.datetime.utcfromtimestamp(mtime)

    return text.replace('{{date_accessed}}', date_accessed.date().isoformat())
