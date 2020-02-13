import os

import earthpy.clip as ec
import geopandas
from shapely.geometry import Polygon

from qgreenland.constants import BBOX_POLYGON


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


def find_shapefile_in_dir(path):
    files = os.listdir(path)
    try:
        f = [x for x in files if x.endswith('.shp')][0]
        return os.path.abspath(os.path.join(path, f))
    except Exception:
        raise RuntimeError(f'No shapefile found in: {files}')
