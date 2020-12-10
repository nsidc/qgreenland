import datetime as dt
import os

from netCDF4 import Dataset

DATASET_ARCHIVE_LOCATION = '/share/appdata/qgreenland-private-archive/esa_cci_gravimetric_mass_balance_dtu/'
DATA_PATH = os.path.join(DATASET_ARCHIVE_LOCATION, 'greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820/CCI_GMB_GIS.nc')

ds = Dataset(DATA_PATH, 'r')
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
times = ds.variables['t'][:]
datas = ds.variables['GMB_trend'][:]
epoch_start = dt.datetime(2003, 1, 1)

for time_idx, time in enumerate(times):
    date = epoch_start + dt.timedelta(days=float(time))
    with open(os.path.join(DATASET_ARCHIVE_LOCATION, f'points_{date:%Y_%m_%d_%H_%M_%S}.csv'), 'w') as f:
        f.write('Latitude, Longitude, GMB_trend\n')
        for lat, lon, data in zip(lats, lons, datas[:, time_idx]):
            f.write(f'{lat}, {lon}, {data}\n')
