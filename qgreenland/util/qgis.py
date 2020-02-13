import os

from osgeo import gdal
import qgis.core as qgc

from qgreenland import PACKAGE_DIR
from qgreenland.constants import BBOX, PROJECT_CRS


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

    basemap_group = project.layerTreeRoot().addGroup('basemap')

    groups = {
        'basemaps': basemap_group,
        'TBD': None,
    }
    # TODO: Parameterize, e.g. below
    #       But then how would we get the ProviderType/ProviderLib?
    #       Just more mapping. But where do we put it? Wrapper class?
    # layer_constructors = {
    #     'raster': qgc.QgsRasterLayer,
    #     'vector': qgc.QgsVectorLayer,
    # }

    for layer_name, layer_cfg in layers_cfg.items():
        # Give the absolute path to the layer. We think project.addMapLayer()
        # automatically generates the correct relative paths. Using a relative
        # path causes statistics (nodata value, min/max) to not be generated,
        # resulting in rendering a gray rectangle.
        # TODO: do we need to worry about differences in path structure between linux
        # and windows?
        layer_path = os.path.join(ROOT_PATH,
                                  layer_cfg['layer_group'],
                                  layer_name,
                                  f"{layer_name}.{layer_cfg['file_type']}")

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

        group = groups[layer_cfg['layer_group']]
        group.addLayer(map_layer)

        # TODO is this necessary? Without adding the map layer to the project (which
        # automatically adds it to the root layer unless `addToLegend` is `False`), the
        # layer added to the basemap does not render.
        project.addMapLayer(map_layer, addToLegend=False)

    # TODO: is it normal to write multiple times?
    project.write()


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
