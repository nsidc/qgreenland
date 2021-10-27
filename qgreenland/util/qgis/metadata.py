import datetime as dt
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

import qgis.core as qgc

from qgreenland.constants import (
    INPUT_DIR,
)
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.util.misc import datasource_dirname
from qgreenland.util.template import load_template


def add_layer_metadata(map_layer: qgc.QgsMapLayer, layer_cfg: ConfigLayer) -> None:
    """Add layer metadata.

    Renders a jinja template to a temporary file location as a valid QGIS qmd
    metadata file. This metadata then gets associated with the `map_layer` using
    its `loadNamedMetadata` method. This metadata gets written to the project
    file when the layer is added to the `project`.
    """
    qmd_template = load_template('metadata.jinja')

    # Set the layer's tooltip
    tooltip = _build_layer_tooltip(layer_cfg)
    map_layer.setAbstract(tooltip)

    # Render the qmd template.
    abstract = build_layer_abstract(layer_cfg)
    layer_extent = map_layer.extent()
    layer_crs = map_layer.crs()

    if layer_cfg.steps:
        provenance_list = [escape(step.provenance) for step in layer_cfg.steps]
    else:
        provenance_list = []

    rendered_qmd = qmd_template.render(
        provenance_list=provenance_list,
        abstract=abstract,
        title=layer_cfg.title,
        crs_proj4_str=layer_crs.toProj4(),
        crs_srsid=layer_crs.srsid(),
        crs_postgres_srid=layer_crs.postgisSrid(),
        crs_authid=layer_crs.authid(),
        crs_description=layer_crs.description(),
        crs_projection_acronym=layer_crs.projectionAcronym(),
        crs_ellipsoid_acronym=layer_crs.ellipsoidAcronym(),
        minx=layer_extent.xMinimum(),
        miny=layer_extent.yMinimum(),
        maxx=layer_extent.xMaximum(),
        maxy=layer_extent.yMaximum(),
    )

    # Write the rendered tempalte to a temporary file
    # location. `map_layer.loadNamedMetadata` expects a string URI corresponding
    # to a file on disk.
    with tempfile.NamedTemporaryFile('w') as temp_file:
        temp_file.write(rendered_qmd)
        temp_file.flush()
        map_layer.loadNamedMetadata(temp_file.name)


def _build_layer_tooltip(layer_cfg: ConfigLayer) -> str:
    """Return a properly escaped layer tooltip text."""
    tt = _build_layer_description(layer_cfg)
    tt += (
        '\n\n'
        'Open Layer Properties and select the Metadata tab for more information.'
    )
    return escape(tt)


def build_layer_abstract(layer_cfg: ConfigLayer) -> str:
    """Return a properly escaped layer abstract text."""
    # Include the layer description first.
    abstract = _build_layer_description(layer_cfg)

    # If the layer has a description, separate it from the abstract of the
    # original data source.
    if abstract:
        abstract += '\n\n=== Original Data Source ===\n'

    abstract += _build_dataset_description(layer_cfg)

    if abstract:
        abstract += '\n\n'

    # Add the dataset's citation
    abstract += _build_dataset_citation(layer_cfg)

    return escape(abstract)


def _build_layer_description(layer_cfg: ConfigLayer) -> str:
    """Return a string representing the layer's description."""
    layer_description = ''

    if cfg_description := layer_cfg.description:
        layer_description += cfg_description

    return layer_description


# TODO: this could take a dataset cfg instead of a layer_cfg and be
# cached. Sometimes multiple layers are derived from the same dataset.
def _build_dataset_description(layer_cfg: ConfigLayer) -> str:
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
def _build_dataset_citation(layer_cfg: ConfigLayer) -> str:
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


def _populate_date_accessed(text: str, *, layer_cfg: ConfigLayer) -> str:
    if '{{date_accessed}}' not in text:
        return text

    ds_dir = datasource_dirname(
        dataset_id=layer_cfg.input.dataset.id,
        asset_id=layer_cfg.input.asset.id,
    )
    fetch_dir = Path(INPUT_DIR) / ds_dir

    # TODO: Use modified time for directory, or latest modified time for files
    # inside?
    mtime = fetch_dir.stat().st_mtime
    date_accessed = dt.datetime.utcfromtimestamp(mtime)

    return text.replace('{{date_accessed}}', date_accessed.date().isoformat())
