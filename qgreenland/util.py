import os

import earthpy.clip as ec
import geopandas
import luigi
import qgis.core as qgc
import requests
import yaml
from shapely.geometry import Polygon

from qgreenland.constants import (DATA_DIR,
                                  DATA_FINAL_DIR,
                                  TaskType)

# TODO: Split this file into many modules:
#       - util/shapefile
#       - util/raster
#       - util/luigi or util/task
#       - util/misc

# TODO: Move stuff to constants
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
REQUEST_TIMEOUT = 3
# NOTE: The order of this dictionary is important for passing to qgc.QgsRectangle
BBOX = {'xmin': -3850000.000, 'ymin': -5350000.0, 'xmax': 3750000.0, 'ymax': 5850000.000}
BBOX_POLYGON = [
    (BBOX['xmin'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymax']),
]
PROJECT_CRS = 'EPSG:3411'


class LayerConfigMixin(luigi.Task):
    layer_cfg = luigi.DictParameter()
    task_type = None

    @property
    def short_name(self):
        return self.layer_cfg['short_name']

    @property
    def outdir(self):
        if self.task_type not in TaskType:
            msg = (f"This class defines self.task_type as '{self.task_type}'. "
                   f'Must be one of: {list(TaskType)}.')
            raise RuntimeError(msg)

        if self.task_type is TaskType.FINAL:
            outdir = (f"{DATA_FINAL_DIR}/{self.layer_cfg['layer_group']}/"
                      f'{self.short_name}')
        else:
            outdir = f'{DATA_DIR}/{self.task_type.value}/{self.short_name}'

        os.makedirs(outdir, exist_ok=True)
        return outdir


def load_layer_config(layername=None):
    LAYERS_CONFIG = os.path.join(THIS_DIR, 'layers.yml')
    with open(LAYERS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)

    if not layername:
        return config

    # TODO: Add error handling
    try:
        return config[layername]
    except KeyError:
        raise NotImplementedError(
            f"Configuration for layer '{layername}' not found."
        )


def fetch_file(url):
    return requests.get(url, timeout=REQUEST_TIMEOUT)


def reproject_shapefile(shapefile):
    gdf = geopandas.read_file(shapefile)
    gdf = gdf.to_crs(epsg=3411)

    return gdf


def subset_shapefile(shapefile):
    input_gdf = geopandas.read_file(shapefile)

    bb_poly = geopandas.GeoSeries([Polygon(BBOX_POLYGON)])
    bb = geopandas.GeoDataFrame({'geometry': bb_poly})
    gdf = ec.clip_shp(input_gdf, bb)

    # /opt/conda/lib/python3.8/site-packages/geopandas/geoseries.py:330:
    # UserWarning: GeoSeries.notna() previously returned False for both missing
    # (None) and empty geometries. Now, it only returns False for missing
    # values. Since the calling GeoSeries contains empty geometries, the result
    # has changed compared to previous versions of GeoPandas.  Given a
    # GeoSeries 's', you can use '~s.is_empty & s.notna()' to get back the old
    # behaviour.

    return gdf[~gdf.is_empty]


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

    for layer_name, layer_cfg in layers_cfg.items():
        layer_path = os.path.join(ROOT_PATH,
                                  layer_cfg['layer_group'],
                                  layer_name,
                                  f"{layer_name}.{layer_cfg['file_type']}")
        # construct a relative path to the coastline layer.
        # TODO: do we need to worry about differences in path structure between linux
        # and windows?
        layer_relpath = os.path.relpath(layer_path, start=os.path.dirname(PROJECT_PATH))

        # https://qgis.org/pyqgis/master/core/QgsVectorLayer.html
        map_layer = qgc.QgsVectorLayer(
            layer_relpath,
            layer_name.capitalize(),  # layer name as it shows up in TOC
            'ogr'  # name of the data provider (memory, postgresql)
        )

        group = groups[layer_cfg['layer_group']]
        group.addLayer(map_layer)

        # TODO is this necessary? Without adding the map layer to the project (which
        # automatically adds it to the root layer unless `addToLegend` is `False`), the
        # layer added to the basemap does not render.
        project.addMapLayer(map_layer, addToLegend=False)

    # TODO: is it normal to write multiple times?
    project.write()
