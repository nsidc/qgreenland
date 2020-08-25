import logging
import subprocess

import geopandas


logger = logging.getLogger('luigi-interface')


def filter_vector(vector_path, *, filter_func):
    gdf = geopandas.read_file(vector_path)

    gdf = gdf.loc[filter_func]
    return gdf


def ogr2ogr(in_filepath, out_filepath, **ogr2ogr_kwargs):
    cmd_args_list = []
    for k, v in ogr2ogr_kwargs.items():
        cmd_args_list.append(f'-{k} {v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (f'. activate gdal && ogr2ogr {cmd_args_str}'
           f' {out_filepath} {in_filepath}')
    logger.debug(f'Executing ogr2ogr command: {cmd}')
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result
