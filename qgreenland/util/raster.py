import logging
import subprocess

import pyproj
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

from qgreenland.constants import CONFIG

logger = logging.getLogger('luigi-interface')


def _get_raster_srs(fp):
    """Read a raster with GDAL and return its SRS or None."""
    try:
        tmp_ds = gdal.Open(fp, GA_ReadOnly)

        # Get WKT projection from gdal
        srs_str = tmp_ds.GetProjection()

        if not srs_str:
            raise Exception('GDAL failed to detect any projection.')

        # Attempt to do better than the WKT from gdal...
        try:
            proj = pyproj.crs.CRS.from_wkt(srs_str)
            return proj.to_string()
        except Exception:
            pass

        # Close the gdal dataset
        del tmp_ds

        return srs_str
    except Exception as e:
        logger.info(f'Failed to detect projection: {e}')
        return None


def warp_raster(inp_path, out_path, *, layer_cfg, warp_kwargs=None):
    logger.info(f"Reprojecting {layer_cfg['id']}...")

    if not warp_kwargs:
        warp_kwargs = {}

    srs_str = _get_raster_srs(inp_path)
    logger.info(f'Detected projection: {srs_str}')

    # Override with configured SRS, if present
    if 'srcSRS' in warp_kwargs:
        logger.info('Overriding the source projection with: '
                    f"{warp_kwargs['srcSRS']}")
        srs_str = warp_kwargs['srcSRS']
    elif not srs_str:
        raise RuntimeError('Not enough information to reproject. '
                           'No projection automatically detected and '
                           'none explicitly provided.')

    project_crs = CONFIG['project']['crs']
    logger.debug(f'Warping with arguments: {warp_kwargs}')
    logger.info(f'Target projection: {project_crs}')
    gdal.Warp(out_path, inp_path, dstSRS=project_crs, **warp_kwargs)


def gdal_calc_raster(in_filepath, out_filepath, *, layer_cfg, gdal_calc_kwargs):
    cmd_args_list = []
    for k, v in gdal_calc_kwargs.items():
        cmd_args_list.append(f'--{k}={v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (f'. activate base && gdal_calc.py {cmd_args_str}'
           f' -A {in_filepath} --outfile={out_filepath}')
    logger.debug(f'Executing gdal_calc command: {cmd}')

    # TODO: util func for running external cmd.
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)
