import earthpy.clip as ec
import geopandas
from shapely.geometry import Polygon

from qgreenland.constants import PROJECT_EXTENT


def bbox_dict_to_polygon(d):
    return Polygon([
        (d['xmin'], d['ymax']),
        (d['xmax'], d['ymax']),
        (d['xmax'], d['ymin']),
        (d['xmin'], d['ymin']),
        (d['xmin'], d['ymax']),
    ])


def reproject_shapefile(shapefile_path):
    gdf = geopandas.read_file(shapefile_path)

    # Some datasets (Natural Earth Ocean shape) come with invalid data (e.g.
    # intersections). The buffer operation cleans those up, but at a
    # significant processing time cost.
    if not gdf.is_valid.all():
        gdf = gdf.buffer(0)

    gdf = gdf.to_crs(epsg=3411)

    return gdf


def subset_shapefile(shapefile, *, layer_cfg):
    if layer_cfg and 'subset_kwargs' in layer_cfg:
        bb = layer_cfg['subset_kwargs']
    else:
        bb = PROJECT_EXTENT
    bb_polygon = geopandas.GeoSeries([bbox_dict_to_polygon(bb)])

    bb_gdf = geopandas.GeoDataFrame({'geometry': bb_polygon})
    input_gdf = geopandas.read_file(shapefile)
    gdf = ec.clip_shp(input_gdf, bb_gdf)

    # /opt/conda/lib/python3.8/site-packages/geopandas/geoseries.py:330:
    # UserWarning: GeoSeries.notna() previously returned False for both missing
    # (None) and empty geometries. Now, it only returns False for missing
    # values. Since the calling GeoSeries contains empty geometries, the result
    # has changed compared to previous versions of GeoPandas.  Given a
    # GeoSeries 's', you can use '~s.is_empty & s.notna()' to get back the old
    # behaviour.

    return gdf[~gdf.is_empty]
