from pathlib import Path
import os
from itertools import product

from netCDF4 import Dataset
import numpy as np


BASE_DIR = Path('/share/appdata/qgreenland-private-archive/racmo_qgreenland_jan2021/')

u_path = BASE_DIR / 'u10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km.YY-mean.nc'
v_path = BASE_DIR / 'v10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km.YY-mean.nc'

u_ds = Dataset(u_path, 'r')
v_ds = Dataset(v_path, 'r')

u_data = u_ds.variables['u10m'][0, 0, :]
v_data = v_ds.variables['v10m'][0, 0, :]

lon_data = u_ds.variables['lon'][:]
lat_data = u_ds.variables['lat'][:]

with open(BASE_DIR / 'wind_vector_points.csv', 'w') as f:
    f.write(f'eastward_component,northward_component,magnitude,lon,lat\n')
    last_i = None
    for i, j in product(range(u_data.shape[0]), range(u_data.shape[1])):
        if i != last_i:
            print(f'Handling row: {i}')
        last_i = i

        u = u_data[i, j]
        if np.ma.is_masked(u):
            continue

        v = v_data[i, j]
        lon = lon_data[i, j]
        lat = lat_data[i, j]
        magnitude = np.sqrt(u**2 + v**2)

        f.write(f'{u},{v},{magnitude},{lon},{lat}\n')
