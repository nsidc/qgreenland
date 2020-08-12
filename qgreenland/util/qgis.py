import os
import subprocess
import tempfile
from xml.sax.saxutils import escape

import qgis.core as qgc
from jinja2 import Template
from osgeo import gdal

from qgreenland import __version__
from qgreenland.constants import (ASSETS_DIR,
                                  CONFIG,
                                  PROJECT_CRS,
                                  PROJECT_EXTENT)
from qgreenland.util.misc import get_layer_fs_path


def create_raster_map_layer(layer_path, layer_cfg):
    # Generate statistics for the raster layer. This creates an `aux.xml` file
    # alongside the .tif file that includes statistics (min/max/std) that qgis
    # can read.
    # Note that generating this file before creating the map layer allows the
    # layer's statistics to be correctly initialized.
    gdal.Info(layer_path, stats=True)

    map_layer = qgc.QgsRasterLayer(
        layer_path,
        layer_cfg['title'],
        'gdal'
    )

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
    tooltip = build_layer_description(layer_cfg)
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
    # Give the absolute path to the layer. We think project.addMapLayer()
    # automatically generates the correct relative paths. Using a relative
    # path causes statistics (nodata value, min/max) to not be generated,
    # resulting in rendering a gray rectangle.
    # TODO: do we need to worry about differences in path structure between linux
    # and windows?
    layer_path = get_layer_fs_path(layer_cfg)

    if not os.path.isfile(layer_path):
        raise RuntimeError(f"Layer located at '{layer_path}' does not exist.")

    # https://qgis.org/pyqgis/master/core/QgsVectorLayer.html
    if layer_cfg['data_type'] == 'vector':
        map_layer = qgc.QgsVectorLayer(
            layer_path,
            layer_cfg['title'],  # layer name as it shows up in QGIS TOC
            'ogr'  # name of the data provider (e.g. memory, postgresql)
        )
    elif layer_cfg['data_type'] == 'raster':
        map_layer = create_raster_map_layer(layer_path, layer_cfg)

    _add_layer_metadata(map_layer, layer_cfg)

    if style := layer_cfg.get('style'):
        load_qml_style(map_layer, style)

    map_layer.setCrs(project_crs)

    return map_layer


def _set_groups_options(project):
    groups_config = CONFIG['layer_groups']

    def _set_group_visibility(group, group_opts):
        # Layer group config is a path of layer groups separated by '/'
        # Group is visible by default.
        group_visible = group_opts.get('visible', True)
        group.setItemVisibilityChecked(group_visible)

    def _set_group_expanded(group, group_opts):
        # Layer group config is a path of layer groups separated by '/'
        # Group is visible by default.
        group_expanded = group_opts.get('expanded', True)
        group.setExpanded(group_expanded)

    for group_path, options in groups_config.items():
        group = _get_or_create_group(project, group_path)

        _set_group_visibility(group, options)
        _set_group_expanded(group, options)


def _get_or_create_group(project, group_path):
    """Get or create the layer group in `project` by `group_path`."""
    group = project.layerTreeRoot()

    # If the group path is an empty string, return the root layer group.
    if not group_path:
        return group

    group_names = group_path.split('/')

    for group_name in group_names:
        if group.findGroup(group_name) is None:
            # Create the group.
            group = group.addGroup(group_name)
        else:
            group = group.findGroup(group_name)

    return group


def _add_layers(project):
    layers_cfg = CONFIG['layers']

    for layer_cfg in layers_cfg.values():
        map_layer = get_map_layer(layer_cfg,
                                  project.crs())

        group_path = layer_cfg.get('group_path', '')
        group = _get_or_create_group(project, group_path)
        # Set layer visibility
        group_layer = group.addLayer(map_layer)
        group_layer.setItemVisibilityChecked(
            # Make the layer visible by default.
            layer_cfg.get('visible', True)
        )

        # All layers start collapsed. When expanded (the default), they show the
        # entire colormap. This takes up a large amount of space in the table of
        # contents.
        group_layer.setExpanded(False)

        # TODO: necessary for root group?
        project.addMapLayer(map_layer, addToLegend=False)


def _add_empty_groups(project):
    groups_config = CONFIG['layer_groups']
    for group_path in groups_config.keys():
        _get_or_create_group(project, group_path)


def make_qgis_project_file(path):
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    # Boilerplate QGIS initialization code;
    # - Suppresses "Application path not intialized" errors
    # - Enables Qt support for fonts used in layer styles (labels)
    qgis_path = subprocess.run(
        ['which', 'qgis'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8').strip('\n')
    qgs = qgc.QgsApplication([], False)
    qgs.initQgis()
    qgc.QgsApplication.setPrefixPath(qgis_path, True)

    # Create a new project; initializes basic structure
    project = qgc.QgsProject.instance()
    project.write(path)

    project_crs = qgc.QgsCoordinateReferenceSystem(PROJECT_CRS)
    project.setCrs(project_crs)

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()
    extent = qgc.QgsReferencedRectangle(
        qgc.QgsRectangle(*PROJECT_EXTENT.values()),
        project_crs
    )
    view.setDefaultViewExtent(extent)

    _add_layers(project)

    _add_decorations(project)

    _set_groups_options(project)

    _add_empty_groups(project)

    # TODO: is it normal to write multiple times?
    project.write()

    # Release all file locks! If we don't do this, we won't be able to clean up
    # layer source files after zipping the project.
    project.clear()


def _add_decorations(project):
    # Add CopyrightLabel:
    project.writeEntry('CopyrightLabel', '/Enabled', True)
    # project.writeEntry('CopyrightLabel', '/FontName', 'Sans Serif')
    # NOTE: Does the copyright symbol work this way or should we use HTML codes?
    copyright_label = f'QGreenland {__version__} © NSIDC 2020'
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


def load_qml_style(map_layer, style_name):
    style_path = os.path.join(ASSETS_DIR, 'styles', style_name + '.qml')
    # If you pass a path to nothing, it will silently fail
    if not os.path.isfile(style_path):
        raise RuntimeError(f"Style '{style_path}' not found.")

    msg, status = map_layer.loadNamedStyle(style_path)

    if not status:
        raise RuntimeError(f"Problem loading '{style_path}': '{msg}'")


def build_layer_description(layer_cfg):
    description = ''

    if cfg_description := layer_cfg.get('description'):
        description += cfg_description
        description += '\n\n=== Original Data Source ===\n'

    dataset_metadata = layer_cfg['dataset']['metadata']
    description += dataset_metadata['title']

    if abstract := dataset_metadata.get('abstract'):
        description += '\n\n'
        description += abstract

    return escape(description)


def build_layer_abstract(layer_cfg):
    abstract = build_layer_description(layer_cfg)

    if abstract:
        abstract += '\n\n'

    dataset_metadata = layer_cfg['dataset']['metadata']
    if citation_cfg := dataset_metadata.get('citation'):
        if citation_text := citation_cfg.get('text'):
            abstract += 'Citation:\n'
            abstract += citation_text + '\n\n'

        if citation_url := citation_cfg.get('url'):
            abstract += 'Citation URL:\n'
            abstract += citation_url

    return escape(abstract)
