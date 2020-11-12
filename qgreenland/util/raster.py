import logging
import os
import subprocess
import tempfile

import pyproj
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

from qgreenland.config import CONFIG

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
    """Use gdal.Warp to modify raster data file.

    TODO: Switch to gdal command-line
    TODO: Figure out a way to warp in one step, stop using _gdalwarp_cut_hack()
    """
    logger.info(f"Reprojecting {layer_cfg['id']}...")

    if not warp_kwargs:
        warp_kwargs = {}

    warp_kwargs['dstSRS'] = CONFIG['project']['crs']

    srs_str = _get_raster_srs(inp_path)
    logger.info(f'Detected projection: {srs_str}')

    # Override with configured srcSRS, if present
    if 'srcSRS' in warp_kwargs:
        logger.info('Overriding the source projection with: '
                    f"{warp_kwargs['srcSRS']}")
        srs_str = warp_kwargs['srcSRS']
    elif not srs_str:
        raise RuntimeError('Not enough information to reproject. '
                           'No projection automatically detected and '
                           'none explicitly provided.')

    # gdal.Warp(out_path, inp_path, **warp_kwargs)
    _gdalwarp_cut_hack(
        out_path, inp_path,
        layer_cfg=layer_cfg, warp_kwargs=warp_kwargs
    )


def _gdalwarp_cut_hack(out_path, inp_path, *, layer_cfg, warp_kwargs):
    """Hack for an issue with some gdal cutlines.

    <mailing list link here>

    Warp and set extent. In order for cut to behave correctly, we have to set
    the target extent (-te in CLI) before doing the cut; if we don't do this,
    gdalwarp returns errors in certain cases:

     Processing NE2_LR_LC_SR_W.tif [1/1] : 0
     Warning 1: Self-intersection at or near point 16155.00500979846
     2024.9999689849035
     ERROR 1: Cutline polygon is invalid.

    We believe this only occurs when the cutline crosses over a "projection
    boundary"; e.g. +/- 180° in WGS84 to polarstereo reprojection. The error
    message above was produced while attempting to reproject NE2 raster to
    polarstereo and cut it along 40° latitude in one operation. We have no
    idea why setting target extent in a separate operation fixes this. Setting
    target extent in the same operation _does not_ fix this.

    TODO: Figure out a way to stop doing this in two steps!!!
    """
    # These kwargs are only for step2. 'creationOptions' is extracted so we
    # don't, e.g. compress twice.
    step2_keys = ['cutlineDSName', 'cropToCutline', 'creationOptions']

    # Step 1 needs to subset for this to work (outputBounds == `-te`).
    step1_kwargs = {k: v for k, v in warp_kwargs.items() if k not in step2_keys}
    step1_kwargs['outputBounds'] = layer_cfg['boundary']['bbox']

    # Step 2 actually does the shape-based cut as a separate step, to avoid
    # errors.
    step2_kwargs = {k: v for k, v in warp_kwargs.items() if k in step2_keys}

    with tempfile.TemporaryDirectory() as td:
        step1_tempfn = f'tempfile{os.path.splitext(out_path)[1]}'
        step1_tempfp = os.path.join(td, step1_tempfn)

        _gdalwarp(step1_tempfp, inp_path, **step1_kwargs)
        _gdalwarp(out_path, step1_tempfp, **step2_kwargs)


def _gdalwarp(out_path, inp_path, **warp_kwargs):
    logger.debug(f'Warping {inp_path} -> {out_path} with arguments:'
                 f' {warp_kwargs}')
    gdal.Warp(out_path, inp_path, **warp_kwargs)


def gdal_calc_raster(in_filepath, out_filepath, *, layer_cfg, gdal_calc_kwargs):
    cmd_args_list = []
    for k, v in gdal_calc_kwargs.items():
        cmd_args_list.append(f'--{k}={v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (f'. activate gdal && gdal_calc.py {cmd_args_str}'
           f' -A {in_filepath} --outfile={out_filepath}')
    logger.debug(f'Executing gdal_calc command: {cmd}')

    # TODO: util func for running external cmd.
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def gdal_mdim_translate_raster(in_filepath, out_filepath, *,
                               layer_cfg, gdal_mdim_translate_kwargs):
    cmd_args_list = []
    for k, v in gdal_mdim_translate_kwargs.items():
        cmd_args_list.append(f'-{k} {v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (f'. activate gdal && gdalmdimtranslate {cmd_args_str}'
           f' {in_filepath} {out_filepath}')
    logger.debug(f'Executing gdalmdimtranslate command: {cmd}')

    # TODO: util func for running external cmd.
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def gdal_edit_raster(in_filepath, *,
                     layer_cfg, gdal_edit_kwargs):
    """Overwrite in_filepath with edited metadata."""
    cmd_args_list = []
    for k, v in gdal_edit_kwargs.items():
        cmd_args_list.append(f'-{k} {v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (
        f'. activate gdal && gdal_edit.py'
        f' {cmd_args_str}'
        f' {in_filepath}'
    )
    logger.debug(f'Executing gdal_edit.py command: {cmd}')

    # TODO: util func for running external cmd.
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)
