import os

import qgis.core as qgc
from osgeo import gdal

from qgreenland import PACKAGE_DIR, __version__
from qgreenland.constants import BBOX, PROJECT_CRS
from qgreenland.util.misc import get_layer_fs_path, load_group_config, load_layer_config


def create_raster_map_layer(layer_path, layer_cfg):
    # Generate statistics for the raster layer. This creates an `aux.xml` file
    # alongside the .tif file that includes statistics (min/max/std) that qgis
    # can read.
    # Note that generating this file before creating the map layer allows the
    # layer's statistics to be correctly initialized.
    gdal.Info(layer_path, stats=True)

    map_layer = qgc.QgsRasterLayer(
        layer_path,
        layer_cfg['name'],
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


def get_map_layer(layer_name, layer_cfg, project_crs, root_path):
    # Give the absolute path to the layer. We think project.addMapLayer()
    # automatically generates the correct relative paths. Using a relative
    # path causes statistics (nodata value, min/max) to not be generated,
    # resulting in rendering a gray rectangle.
    # TODO: do we need to worry about differences in path structure between linux
    # and windows?
    layer_path = get_layer_fs_path(layer_name, layer_cfg)

    if not os.path.isfile(layer_path):
        raise RuntimeError(f"Layer path '{layer_path}' does not exist.")

    # https://qgis.org/pyqgis/master/core/QgsVectorLayer.html
    if layer_cfg['data_type'] == 'vector':
        map_layer = qgc.QgsVectorLayer(
            layer_path,
            layer_cfg['name'],  # layer name as it shows up in TOC
            'ogr'  # name of the data provider (memory, postgresql)
        )
    elif layer_cfg['data_type'] == 'raster':
        map_layer = create_raster_map_layer(layer_path, layer_cfg)

    map_layer.setAbstract(build_abstract(layer_cfg))

    # TODO: COO COO CACHOO
    if layer_cfg.get('style'):
        load_qml_style(map_layer, layer_cfg.get('style'))

    map_layer.setCrs(project_crs)

    return map_layer


def _set_groups_options(project):
    groups_config = load_group_config()

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
        group = _get_group(project, group_path)

        _set_group_visibility(group, options)
        _set_group_expanded(group, options)


def _make_layer_groups(project):
    """Read the layer group config yaml and add those groups to `project`."""
    groups_config = load_group_config()

    for group_path, options in groups_config.items():
        group = project.layerTreeRoot()
        for group_name in group_path.split('/'):
            # Get or create the group.
            if group.findGroup(group_name) is None:
                group = group.addGroup(group_name)
            else:
                group = group.findGroup(group_name)


def _get_group(project, group_path):
    """Look up layer group in `project` by `group_path`."""
    group = project.layerTreeRoot()

    # If the group path is an empty string, return the root layer group.
    if not group_path:
        return group

    group_names = group_path.split('/')

    for idx, group_name in enumerate(group_names):
        # TODO: COO COO CACHOO
        if group.findGroup(group_name) is None:
            parent_path = '/'.join(group_names[:idx])
            raise KeyError(f"Group '{group_name}' under "
                           f"parent '{parent_path}' not found.")

        group = group.findGroup(group_name)

    return group


def _add_layers(project):
    layers_cfg = load_layer_config()
    for layer_name, layer_cfg in layers_cfg.items():
        layer_cfg = layers_cfg[layer_name]
        map_layer = get_map_layer(layer_name,
                                  layer_cfg,
                                  project.crs(),
                                  project.absolutePath())

        layer_path = layer_cfg.get('path', '')
        group = _get_group(project, layer_path)
        # Set layer visibility
        group_layer = group.addLayer(map_layer)
        group_layer.setItemVisibilityChecked(
            # Make the layer visible by default.
            layer_cfg.get('visible', True)
        )

        # TODO: necessary for root group?
        project.addMapLayer(map_layer, addToLegend=False)


def make_qgs(path):
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    project = qgc.QgsProject.instance()

    # Create a new project; initializes basic structure
    project.write(path)

    project_crs = qgc.QgsCoordinateReferenceSystem(PROJECT_CRS)
    project.setCrs(project_crs)

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()
    extent = qgc.QgsReferencedRectangle(qgc.QgsRectangle(*BBOX.values()),
                                        project_crs)
    view.setDefaultViewExtent(extent)

    _make_layer_groups(project)

    _add_layers(project)

    _add_decorations(project)

    _set_groups_options(project)

    _fix_layer_order(project)

    # TODO: is it normal to write multiple times?
    project.write()


def _fix_layer_order(project):
    """HACK. QGIS automatically selects and expands the first layer in the legend.

    Force the coastlines layer to be first in the basemaps group so that the
    first group state is correct (when this was written, bedmachine incorrectly
    shows up as 'expanded' in the legend).
    """
    basemaps_group = _get_group(project, 'basemaps')
    layers = basemaps_group.findLayers()
    for layer in layers:
        if 'coastlines' in layer.name().lower():
            cloned_layer = layer.clone()
            basemaps_group.removeChildNode(layer)
            basemaps_group.insertChildNode(0, cloned_layer)
            break


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
    style_path = os.path.join(PACKAGE_DIR, 'styles', style_name + '.qml')
    # If you pass a path to nothing, it will silently fail
    if not os.path.isfile(style_path):
        raise RuntimeError(f"Style '{style_path}' not found.")

    msg, status = map_layer.loadNamedStyle(style_path)

    if not status:
        raise RuntimeError(f"Problem loading '{style_path}': '{msg}'")


def build_abstract(layer_cfg):
    abstract = ''
    if layer_cfg.get('description'):
        abstract += layer_cfg['description'] + '\n\n'

    if layer_cfg.get('abstract'):
        abstract += 'Abstract:\n'
        abstract += layer_cfg['abstract'] + '\n\n'

    if layer_cfg.get('citation'):
        if layer_cfg['citation'].get('text'):
            abstract += 'Citation:\n'
            abstract += layer_cfg['citation']['text'] + '\n\n'

        if layer_cfg['citation'].get('url'):
            abstract += 'Citation URL:\n'
            abstract += layer_cfg['citation']['url']

    return abstract
