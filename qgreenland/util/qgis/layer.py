import functools
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Union
from xml.sax.saxutils import escape

import qgis.core as qgc
from osgeo import gdal

import qgreenland.exceptions as exc
from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.layer import Layer
from qgreenland.util.layer import get_layer_compile_filepath, vector_or_raster
from qgreenland.util.metadata import build_layer_description, build_layer_metadata
from qgreenland.util.template import load_template
from qgreenland.util.tree import LayerNode


def _build_layer_tooltip(layer_cfg: Layer) -> str:
    """Return a properly escaped layer tooltip text."""
    tt = build_layer_description(layer_cfg)
    tt += (
        "\n\n" "Open Layer Properties and select the Metadata tab for more information."
    )
    return escape(tt)


def add_layer_metadata(map_layer: qgc.QgsMapLayer, layer_cfg: Layer) -> None:
    """Add layer metadata.

    Renders a jinja template to a temporary file location as a valid QGIS qmd
    metadata file. This metadata then gets associated with the `map_layer` using
    its `loadNamedMetadata` method. This metadata gets written to the project
    file when the layer is added to the `project`.
    """
    qmd_template = load_template("metadata.jinja")

    # Set the layer's tooltip
    tooltip = _build_layer_tooltip(layer_cfg)
    map_layer.setAbstract(tooltip)

    # Render the qmd template.
    abstract = escape(build_layer_metadata(layer_cfg))
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
    with tempfile.NamedTemporaryFile("w") as temp_file:
        temp_file.write(rendered_qmd)
        temp_file.flush()
        map_layer.loadNamedMetadata(temp_file.name)


def make_map_layer(layer_node: LayerNode) -> qgc.QgsMapLayer:
    layer_path = _layer_path(
        layer_node=layer_node,
    )
    layer_type = vector_or_raster(layer_node)
    if layer_type == "Vector":
        provider = "ogr"
        qgs_layer_creator = qgc.QgsVectorLayer
    elif layer_type == "Raster":
        provider = "gdal"
        qgs_layer_creator = qgc.QgsRasterLayer

    # For online layers, the provider is specified in the config.
    layer_cfg = layer_node.layer_cfg
    if type(layer_cfg.input.asset) is OnlineAsset:
        provider = layer_cfg.input.asset.provider

    creator = functools.partial(
        qgs_layer_creator,
        str(layer_path),
        layer_cfg.title,
        provider,
    )
    map_layer = _create_layer_with_side_effects(
        creator,
        layer_node=layer_node,
    )

    if not map_layer.isValid():
        raise exc.QgrRuntimeError(
            f"Invalid QgsMapLayer created for layer {layer_cfg.id}",
        )

    add_layer_metadata(map_layer, layer_cfg)

    if style_filepath := layer_cfg.style_filepath:
        _load_qml_style(map_layer, style_filepath)

    return map_layer


def _layer_path(
    layer_node: LayerNode,
) -> Union[Path, str]:
    layer_cfg = layer_node.layer_cfg
    if type(layer_cfg.input.asset) is OnlineAsset:
        return f"{layer_cfg.input.asset.url}"
    else:
        # Give the absolute path to the layer. We think project.addMapLayer()
        # automatically generates the correct relative paths. Using a relative
        # path causes statistics (nodata value, min/max) to not be generated,
        # resulting in rendering a gray rectangle.
        return get_layer_compile_filepath(layer_node)


def _offline_raster_side_effects(
    creator: Callable[..., qgc.QgsRasterLayer],
    *,
    layer_node: LayerNode,
) -> qgc.QgsRasterLayer:
    """Generate raster statistics on disk and in the layer object."""
    layer_path = _layer_path(layer_node)

    # Create .aux.xml metadatafile with raster band statistics; useful
    # for styling and accurate min/max/stdev/mean in QGIS layer info
    # panel
    gdal.Info(str(layer_path), stats=True)

    map_layer = creator()

    # Set the min/max render accuracy to 'Exact'. Usually qgis estimates
    # statistics for e.g., generating the default colormap.
    mmo = map_layer.renderer().minMaxOrigin()
    mmo.setStatAccuracy(0)  # 0 == 'Exact'
    map_layer.renderer().setMinMaxOrigin(mmo)

    return map_layer


def _create_layer_with_side_effects(
    creator: Callable[..., qgc.QgsMapLayer],
    *,
    layer_node: LayerNode,
) -> qgc.QgsMapLayer:
    """Apply special steps before/after creating a layer."""
    layer_cfg = layer_node.layer_cfg
    layer_type = vector_or_raster(layer_node)

    offline_raster = (
        layer_type == "Raster" and type(layer_cfg.input.asset) is not OnlineAsset
    )

    if offline_raster:
        return _offline_raster_side_effects(creator, layer_node=layer_node)
    else:
        return creator()


def _load_qml_style(map_layer: qgc.QgsMapLayer, style_path: Path) -> None:
    msg, status = map_layer.loadNamedStyle(str(style_path))

    if not status:
        raise RuntimeError(f"Problem loading '{style_path}': '{msg}'")
