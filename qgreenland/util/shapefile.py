import subprocess

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


def reproject_shapefile(shapefile_path, *, layer_cfg):
    """Reprojects a shapefile and returns the result."""
    gdf = geopandas.read_file(shapefile_path)

    # Some datasets (Natural Earth Ocean shape) come with invalid data (e.g.
    # intersections). The buffer operation cleans those up, but at a
    # significant processing time cost.

    if 'override_source_projection' in layer_cfg:
        gdf.crs = layer_cfg['override_source_projection']

    gdf = gdf.to_crs(epsg=3411)

    return gdf


def subset_shapefile(shapefile, *, layer_cfg, outfile):
    """Subsets a shapefile and writes the output."""
    # NOTE: This function originally used earthpy.clip.clip_shp, but this was
    # retuning an empty dataframe for certain multipolygons (e.g. NE Ocean).
    # Also, using earthpy.clip.clip_shp would unexpectedly remove some
    # polygons, e.g. NE Land's North America polygon.

    if layer_cfg and 'subset_kwargs' in layer_cfg:
        bb = layer_cfg['subset_kwargs']
    else:
        bb = PROJECT_EXTENT

    clipsrc_arg = '-clipsrc "{xmin}" "{ymin}" "{xmax}" "{ymax}" '.format(**bb)  # noqa
    cmd = f'. activate base && ogr2ogr {clipsrc_arg} {outfile} {shapefile}'

    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)
