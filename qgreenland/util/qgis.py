import datetime as dt
import logging
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional
from xml.sax.saxutils import escape

import qgis.core as qgc
from PyQt5.QtGui import QColor
from jinja2 import Template
from osgeo import gdal

from qgreenland.config import CONFIG
from qgreenland.constants import ASSETS_DIR, INPUT_DIR
from qgreenland.exceptions import QgrInvalidConfigError
from qgreenland.util.misc import (
    datasource_dirname,
    get_final_layer_filepath,
    vector_or_raster,
)
from qgreenland.util.version import get_build_version

logger = logging.getLogger('luigi-interface')
LAYERGROUP_EXPANDED_DEFAULT = False
LAYERGROUP_VISIBLE_DEFAULT = False

# TODO: Figure out which functions should start with underscore and apply
# consistently


# TODO: _create_raster_layer? Pass in "title" instead of "layer_cfg"?
def _get_raster_layer(layer_path: Path, layer_cfg: Dict[Any, Any]):
    # TODO: Does qgis have types that can catch passing a Path here?
    return qgc.QgsRasterLayer(
        str(layer_path),
        layer_cfg['title'],
        'gdal'
    )


def create_raster_map_layer(layer_path: Path, layer_cfg: Dict[Any, Any]):
    # TODO: Re-implement
    # if layer_cfg['dataset']['access_method'] == 'gdal_remote':
    #     return _get_raster_layer(layer_path, layer_cfg)

    # Generate statistics for the raster layer. This creates an `aux.xml` file
    # alongside the .tif file that includes statistics (min/max/std) that qgis
    # can read.
    # Note that generating this file before creating the map layer allows the
    # layer's statistics to be correctly initialized.

    # TODO: Does gdal have types that can throw an error if a `Path` is passed?
    # If not, write stubs!
    gdal.Info(str(layer_path), stats=True)

    map_layer = _get_raster_layer(layer_path, layer_cfg)

    # Set the min/max render accuracy to 'Exact'. Usually qgis estimates
    # statistics for e.g., generating the default colormap.
    mmo = map_layer.renderer().minMaxOrigin()
    # 0 == 'Exact'
    # map_layer.renderer().minMaxOrigin().statAccuracyString(0)
    mmo.setStatAccuracy(0)
    map_layer.renderer().setMinMaxOrigin(mmo)

    return map_layer


def _add_layer_metadata(map_layer, layer_cfg):
    """Add layer metadata.

    Renders a jinja template to a temporary file location as a valid QGIS qmd
    metadata file. This metadata then gets associated with the `map_layer` using
    its `loadNamedMetadata` method. This metadata gets written to the project
    file when the layer is added to the `project`.
    """
    # Load/render the template.
    template_path = os.path.join(ASSETS_DIR, 'templates', 'metadata.jinja')
    with open(template_path, 'r') as f:
        qmd_template_str = ' '.join(f.readlines())

    # Set the layer's tooltip
    tooltip = build_layer_tooltip(layer_cfg)
    map_layer.setAbstract(tooltip)

    # Render the qmd template.
    abstract = build_layer_abstract(layer_cfg)
    layer_extent = map_layer.extent()
    qmd_template = Template(qmd_template_str)
    rendered_qmd = qmd_template.render(
        abstract=abstract,
        title=layer_cfg['title'],
        minx=layer_extent.xMinimum(),
        miny=layer_extent.yMinimum(),
        maxx=layer_extent.xMaximum(),
        maxy=layer_extent.yMaximum()
    )

    # Write the rendered tempalte to a temporary file
    # location. `map_layer.loadNamedMetadata` expects a string URI corresponding
    # to a file on disk.
    with tempfile.NamedTemporaryFile('w') as temp_file:
        temp_file.write(rendered_qmd)
        temp_file.flush()
        map_layer.loadNamedMetadata(temp_file.name)


def get_map_layer(layer_cfg, project_crs):
    """Create Qgs layer objects from layer config."""
    # Give the absolute path to the layer. We think project.addMapLayer()
    # automatically generates the correct relative paths. Using a relative
    # path causes statistics (nodata value, min/max) to not be generated,
    # resulting in rendering a gray rectangle.
    # TODO: do we need to worry about differences in path structure between linux
    # and windows?
    layer_path = get_final_layer_filepath(layer_cfg)
    # TODO: LayerType definition
    layer_type = vector_or_raster(layer_path)

    # https://qgis.org/pyqgis/master/core/QgsVectorLayer.html
    if layer_type == 'Vector':
        map_layer = qgc.QgsVectorLayer(
            str(layer_path),
            layer_cfg['title'],  # layer name as it shows up in QGIS TOC
            'ogr'  # name of the data provider (e.g. memory, postgresql)
        )
    elif layer_type == 'Raster':
        map_layer = create_raster_map_layer(layer_path, layer_cfg)

    _add_layer_metadata(map_layer, layer_cfg)

    if style := layer_cfg.get('style'):
        load_qml_style(map_layer, style)

    if layer_crs := layer_cfg.get('project_crs'):
        map_layer.setCrs(qgc.QgsCoordinateReferenceSystem(layer_crs))
    else:
        map_layer.setCrs(project_crs)

    return map_layer


def _set_group_visibility(group, visibility: bool):
    group.setItemVisibilityChecked(visibility)


def _set_group_expanded(group, expanded: bool):
    group.setExpanded(expanded)


# TODO: Type `project` (QgsProject?) and return (`QgsGroup`?)`
def _get_group(
    project: qgc.QgsProject,
    group_path: List['str'],
) -> Optional[qgc.QgsLayerTreeGroup]:
    """Find a group in `project` from ordered list of group names.

    e.g. group_path: `['parent', 'child', 'grandchild']`
    """
    group = project.layerTreeRoot()

    # If the group path is an empty string, return the root layer group
    if not group_path:
        return group

    for group_name in group_path:
        group = group.findGroup(group_name)

        # Group not found
        if group is None:
            # TODO: Raise instead of return None?
            return None

    return group


def _ensure_group_exists(project, group_path):
    """Get or create the layer group in `project` by `group_path`."""
    if group := _get_group(project, group_path):
        return group

    group_names = group_path.split('/')

    # Create the group path from the ground up; it's OK if part of the path
    # already exists.
    group = project.layerTreeRoot()
    for group_name in group_names:
        if g := group.findGroup(group_name):
            group = g
            continue

        group = group.addGroup(group_name)

        # Set default configuration
        _set_group_visibility(group, LAYERGROUP_VISIBLE_DEFAULT)
        _set_group_expanded(group, LAYERGROUP_EXPANDED_DEFAULT)

    return group


def _set_groups_options(project):
    logger.debug('Configuring layer groups...')
    groups_config = CONFIG['layer_groups']

    for group_path, options in groups_config.items():
        group = _get_group(project, group_path)

        if group is None:
            # TODO: check for this case in config validation/linting.
            # raise QgrInvalidConfigError(
            logger.error(
                f"Encountered group '{group_path}' without reference in"
                ' layers.yml. Ignoring.'
            )
            return

        _set_group_visibility(
            group,
            options.get('visible', LAYERGROUP_VISIBLE_DEFAULT)
        )
        _set_group_expanded(
            group,
            options.get('expanded', LAYERGROUP_EXPANDED_DEFAULT)
        )

        logger.debug(f'{group_path} configured: {options}')

    logger.debug('Done configuring layer groups.')


def _add_layers(project):
    logger.debug('Adding layers...')
    layers_cfg = CONFIG['layers']

    for layer_cfg in layers_cfg.values():
        logger.debug(f"Adding {layer_cfg['id']}...")
        map_layer = get_map_layer(layer_cfg,
                                  project.crs())

        group_path = layer_cfg.get('group_path', '')
        group = _ensure_group_exists(project, group_path)
        group_layer = group.addLayer(map_layer)
        # Make the layer invisible and collapsed by default
        group_layer.setItemVisibilityChecked(
            layer_cfg.get('visible', False)
        )

        # All layers start collapsed. When expanded (the default), they show the
        # entire colormap. This takes up a large amount of space in the table of
        # contents.
        group_layer.setExpanded(False)

        # TODO: necessary for root group?
        project.addMapLayer(map_layer, addToLegend=False)

    logger.debug('Done adding layers.')


def make_qgis_project_file(path):
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    # The qgis prefix path is two directories above the qgis executable.
    # See:
    # https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    qgis_path = subprocess.run(
        ['which', 'qgis'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8').strip('\n')
    qgis_prefix_path = os.path.abspath(os.path.join(qgis_path, '..', '..'))

    # Boilerplate QGIS initialization code;
    # - Suppresses "Application path not intialized" errors
    # - Enables Qt support for fonts used in layer styles (labels)
    qgs = qgc.QgsApplication([], False)
    qgs.initQgis()
    qgc.QgsApplication.setPrefixPath(qgis_prefix_path, True)

    # Create a new project; initializes basic structure
    project = qgc.QgsProject.instance()
    project.write(path)

    project_crs = qgc.QgsCoordinateReferenceSystem(CONFIG['project']['crs'])
    project.setCrs(project_crs)

    # Set the map background color to be gray (same color as Quantarctica)
    project.setBackgroundColor(QColor(200, 200, 200))

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()

    project_rectangle = qgc.QgsReferencedRectangle(
        qgc.QgsRectangle(
            *CONFIG['project']['boundaries']['data']['bbox']
        ),
        project_crs
    )
    view.setDefaultViewExtent(project_rectangle)

    _add_layers(project)

    _add_decorations(project)

    _set_groups_options(project)

    # TODO: is it normal to write multiple times?
    project.write()

    # Release all file locks! If we don't do this, we won't be able to clean up
    # layer source files after zipping the project.
    project.clear()


def _add_decorations(project):
    logger.debug('Adding decorations...')
    # Add CopyrightLabel:
    project.writeEntry('CopyrightLabel', '/Enabled', True)
    # project.writeEntry('CopyrightLabel', '/FontName', 'Sans Serif')
    # NOTE: Does the copyright symbol work this way or should we use HTML codes?
    year = dt.date.today().year
    copyright_label = escape(
        f'QGreenland {get_build_version()} © NSIDC {year}'
        '\nhttps://qgreenland.org | https://github.com/nsidc/qgreenland/'
    )
    project.writeEntry('CopyrightLabel', '/Label', copyright_label)
    project.writeEntry('CopyrightLabel', '/Placement', 0)
    project.writeEntry('CopyrightLabel', '/MarginH', 0)
    project.writeEntry('CopyrightLabel', '/MarginV', 0)

    # Add Image (QGreenland logo):
    project.writeEntry('Image', '/Enabled', True)
    project.writeEntry('Image', '/Placement', 0)
    project.writeEntry('Image', '/MarginH', 4)
    project.writeEntry('Image', '/MarginV', 8)
    project.writeEntry('Image', '/Size', 24)
    project.writeEntry('Image', '/ImagePath', 'qgreenland.png')

    logger.debug('Done adding decorations.')


def load_qml_style(map_layer, style_name):
    style_path = os.path.join(ASSETS_DIR, 'styles', style_name + '.qml')
    # If you pass a path to nothing, it will silently fail
    if not os.path.isfile(style_path):
        raise RuntimeError(f"Style '{style_path}' not found.")

    msg, status = map_layer.loadNamedStyle(style_path)

    if not status:
        raise RuntimeError(f"Problem loading '{style_path}': '{msg}'")


def _build_layer_description(layer_cfg):
    """Return a string representing the layer's description."""
    layer_description = ''

    if cfg_description := layer_cfg.get('description'):
        layer_description += cfg_description

    return layer_description


def build_layer_tooltip(layer_cfg):
    """Return a properly escaped layer tooltip text."""
    tt = _build_layer_description(layer_cfg)
    tt += (
        '\n\n'
        'Open Layer Properties and select the Metadata tab for more information.'
    )
    return escape(tt)


def _build_dataset_description(layer_cfg):
    """Return a string representing the layer's dataset description."""
    dataset_description = ''

    dataset_metadata = layer_cfg['dataset']['metadata']
    dataset_description += dataset_metadata['title']

    if abstract := dataset_metadata.get('abstract'):
        dataset_description += '\n\n'
        dataset_description += abstract

    return dataset_description


def _build_dataset_citation(layer_cfg):
    """Return a string representing the layer's dataset citation."""
    citation = ''

    dataset_metadata = layer_cfg['dataset']['metadata']
    if citation_cfg := dataset_metadata.get('citation'):
        if citation_text := citation_cfg.get('text'):
            ct = _populate_date_accessed(citation_text, layer_cfg=layer_cfg)
            citation += 'Citation:\n'
            citation += ct + '\n\n'

        if citation_url := citation_cfg.get('url'):
            citation += 'Citation URL:\n'
            citation += citation_url

    return citation


def _populate_date_accessed(text: str, *, layer_cfg):
    if '{{date_accessed}}' not in text:
        return text

    ds_dir = datasource_dirname(
        dataset_id=layer_cfg['dataset']['id'],
        asset_id=layer_cfg['asset']['id'],
    )
    fetch_dir = Path(INPUT_DIR) / ds_dir

    # TODO: Use modified time for directory, or latest modified time for files
    # inside?
    mtime = fetch_dir.stat().st_mtime
    date_accessed = dt.datetime.utcfromtimestamp(mtime)

    return text.replace('{{date_accessed}}', date_accessed.date().isoformat())


def build_layer_abstract(layer_cfg):
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
