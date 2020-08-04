import logging
import subprocess

import geopandas
import pyproj
from shapely.geometry import Polygon

from qgreenland.constants import PROJECT_CRS, PROJECT_EXTENT

logger = logging.getLogger('luigi-interface')


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

    logger.info(f"Reprojecting {layer_cfg['id']}...")
    try:
        proj_str = pyproj.crs.CRS.from_dict(gdf.crs).to_string()
        logger.info(f'Detected source projection: {proj_str}')
    except Exception as e:
        logger.info(f'Failed to detect source projection: {e}')

    # Some datasets (Natural Earth Ocean shape) come with invalid data (e.g.
    # intersections). The buffer operation cleans those up, but at a
    # significant processing time cost.

    if 'override_source_projection' in layer_cfg:
        logger.info('Using source projection from config: '
                    f"{layer_cfg['override_source_projection']}")
        gdf.crs = layer_cfg['override_source_projection']

    logger.info(f'Target projection: {PROJECT_CRS}')
    gdf = gdf.to_crs(PROJECT_CRS)

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
