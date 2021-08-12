import logging
import subprocess

import geopandas as gpd
import pandas as pd

from qgreenland.exceptions import QgrRuntimeError

logger = logging.getLogger('luigi-interface')


# TODO: Types!
def points_txt_to_shape(
    in_filepath,
    out_filepath,
    *,
    header,
    delimiter,
    field_names,
    x_field,
    y_field,
):
    """Convert a textfile of points to a vector data file.

    TODO: `ogr2ogr` can operate on delimited text files, but not without a
    header. Perhaps this task could add header to files that don't have one? Or
    pass on the correct info to `ogr2ogr` about what each column represents
    positionally? An example ogr2ogr command:

    $ ogr2ogr -oo X_POSSIBLE_NAMES=lon -oo Y_POSSIBLE_NAMES=lat -a_srs "EPSG:4326" out.shp in.csv  # noqa
    """
    df = pd.read_table(in_filepath, header=header, delimiter=delimiter)

    # If the header is 'none', there is no header and it must be defiend via
    # `field_names`
    if header is None:
        if not field_names or len(field_names) != len(df.columns):
            raise QgrRuntimeError(
                '`field_names` must be a list of field names corresponding to each of the'
                f' {len(df.columns)} columns in {in_filepath}. Got'
                f' {field_names=}',
            )

        df = df.rename(columns={idx: field_names[idx] for idx in range(len(field_names))})

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[x_field], df[y_field]))
    gdf.to_file(out_filepath, driver='GPKG')


# TODO: Take kwargs, args, and env as separate inputs to avoid special cases.
#       This implies separate config keys for each of these as well.
def ogr2ogr(in_filepath, out_filepath, **ogr2ogr_kwargs):
    cmd_args_list = []
    cmd_prefix = ''
    if 'OGR_ENABLE_PARTIAL_REPROJECTION' in ogr2ogr_kwargs.keys():
        enable_partial_reprojection = ogr2ogr_kwargs.pop(
            'OGR_ENABLE_PARTIAL_REPROJECTION',
        )
        cmd_prefix = f'OGR_ENABLE_PARTIAL_REPROJECTION={enable_partial_reprojection}'

    for k, v in ogr2ogr_kwargs.items():
        # NOTE: Sometimes `v` must be multiple args, e.g. xmin ymin xmax ymax;
        # Other times, `v` is a string that must be quoted as one argument. We
        # can't assume which, so the user must do proper quotation in the config
        # file. This sometimes results in horrible YAML quotation messes like:
        #     where: '"\"ZONE\" != 0"'
        cmd_args_list.append(f'-{k} {v}')

    cmd_args_str = ' '.join(cmd_args_list)

    cmd = (f'. activate gdal && {cmd_prefix} ogr2ogr {cmd_args_str}'
           f' {out_filepath} {in_filepath}')
    logger.debug(f'Executing ogr2ogr command: {cmd}')
    result = subprocess.run(cmd,
                            shell=True,
                            executable='/bin/bash',
                            capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result
