import os

import qgis.core as qgc
from osgeo import gdal

from qgreenland import PACKAGE_DIR, __version__
from qgreenland.constants import BBOX, PROJECT_CRS
from qgreenland.util.misc import get_layer_path, load_group_config


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
    layer_path = get_layer_path(layer_name, layer_cfg)

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


# TODO: dry out these funcs!
def _set_group_visibility(group, layer_group_list, group_config):
    # Layer group config is a path of layer groups separated by '/'
    layer_tree_path = '/'.join(layer_group_list)

    # Group is visible by default.
    group_visible = group_config.get(layer_tree_path, {}).get('visible', True)
    group.setItemVisibilityChecked(group_visible)


def _set_group_expanded(group, layer_group_list, group_config):
    # Layer group config is a path of layer groups separated by '/'
    layer_tree_path = '/'.join(layer_group_list)

    # Group is visible by default.
    group_expanded = group_config.get(layer_tree_path, {}).get('expanded', True)
    group.setExpanded(group_expanded)


def make_qgs(layers_cfg, path):
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    # The qgreenland .qgs project file will live at the root of the qgreenland
    # package distributed to end users.
    ROOT_PATH = os.path.dirname(path)

    # TODO: Reconsider normpath
    PROJECT_PATH = os.path.normpath(os.path.join(path))

    # Write your code here to load some layers, use processing algorithms, etc.
    project = qgc.QgsProject.instance()

    # Create a new project; initializes basic structure
    project.write(PROJECT_PATH)
    # An existing project can be opened w/ the `load` method

    # write the project coordinate ref system.
    project_crs = qgc.QgsCoordinateReferenceSystem(PROJECT_CRS)
    project.setCrs(project_crs)

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()
    extent = qgc.QgsReferencedRectangle(qgc.QgsRectangle(*BBOX.values()),
                                        project_crs)
    view.setDefaultViewExtent(extent)

    group_config = load_group_config()

    for layer_name, layer_cfg in layers_cfg.items():
        # Get the list of layer groups
        # A list with elements represent a layer group path. For example, a list
        # ['basemaps', 'bedmachine'] means that this layer should be under the
        # 'bedmachine' layer group, which is itself within the 'basemaps' layer
        # group.
        layer_group_config = layer_cfg.get('layer_group', {})
        layer_group_list = layer_group_config.get('location', [])

        # An empty list indicates that the layer should be placed in the root of
        # the TOC.
        group = project.layerTreeRoot()

        if layer_group_list:
            for group_name in layer_group_list:
                # Get or create the group.
                if group.findGroup(group_name) is None:
                    group = group.addGroup(group_name)
                else:
                    group = group.findGroup(group_name)

            _set_group_visibility(group, layer_group_list, group_config)
            _set_group_expanded(group, layer_group_list, group_config)

        layer_cfg = layers_cfg[layer_name]
        map_layer = get_map_layer(layer_name,
                                  layer_cfg,
                                  project_crs,
                                  ROOT_PATH)

        # Set group layer visibility
        group_layer = group.addLayer(map_layer)
        group_layer.setItemVisibilityChecked(
            # Make the layer visible by default.
            layer_group_config.get('visible', True)
        )

        # TODO: necessary for root group?
        project.addMapLayer(map_layer, addToLegend=False)

    _add_decorations(project)

    # TODO: is it normal to write multiple times?
    project.write()


def _add_decorations(project):
    # Add CopyrightLabel:
    project.writeEntry('CopyrightLabel', '/Enabled', True)
    # project.writeEntry('CopyrightLabel', '/FontName', 'Sans Serif')
    # NOTE: Does the copyright symbol work this way or should we use HTML codes?
    copyright_label = f'QGreenland v{__version__} © NSIDC 2020'
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
