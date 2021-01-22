import os
import subprocess
from itertools import product
from pathlib import Path

from netCDF4 import Dataset
import numpy as np


BASE_DIR = Path('/share/appdata/qgreenland-private-archive/racmo_qgreenland_jan2021/')

# Paths to "u" and "v" directional magnitude components of windspeed vectors
u_path = BASE_DIR / 'u10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km.YY-mean.nc'
v_path = BASE_DIR / 'v10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km.YY-mean.nc'


def _cmd(cmd: str):
    result = subprocess.run(
        cmd,
        shell=True,
        executable='/bin/bash',
        capture_output=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result


def write_csv() -> Path:
    u_ds = Dataset(u_path, 'r')
    v_ds = Dataset(v_path, 'r')

    u_data = u_ds.variables['u10m'][0, 0, :]
    v_data = v_ds.variables['v10m'][0, 0, :]

    lon_data = u_ds.variables['lon'][:]
    lat_data = u_ds.variables['lat'][:]

    csv_path = BASE_DIR / 'wind_vector_points.csv'
    with open(csv_path, 'w') as f:
        f.write(f'eastward_component,northward_component,magnitude,lon,lat\n')
        for i, j in product(range(u_data.shape[0]), range(u_data.shape[1])):
            u = u_data[i, j]
            if np.ma.is_masked(u):
                continue

            v = v_data[i, j]
            lon = lon_data[i, j]
            lat = lat_data[i, j]
            magnitude = np.sqrt(u**2 + v**2)

            f.write(f'{u},{v},{magnitude},{lon},{lat}\n')

    return csv_path

def convert_to_gpkg(in_fp: Path):
    out_fp = BASE_DIR / 'wind_vector_points.gpkg'
    return _cmd(
        'ogr2ogr'
        ' -oo X_POSSIBLE_NAMES=lon'
        ' -oo Y_POSSIBLE_NAMES=lat'
        ' -oo AUTODETECT_TYPE=True'
        ' -s_srs "EPSG:4326" -t_srs "EPSG:3413"'
        f' {out_fp} {in_fp}'
    )


def u_v_to_magnitude_raster():
    out_fp = BASE_DIR / 'magnitudes.tif'

    return _cmd(
        'gdal_calc.py'
        f' -A NETCDF:{u_path}:u10m -B NETCDF:{v_path}:v10m'
        f' --calc="sqrt(A**2 + B**2)" --outfile={out_fp}'
    )


if __name__ == '__main__':
    # Generate magnitude.tif
    u_v_to_magnitude_raster()

    # Generate wind_vector_points.gpkg
    csv_fp = write_csv()
    convert_to_gpkg(csv_fp)
