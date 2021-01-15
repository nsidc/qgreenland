import datetime as dt
import os

import fiona
from fiona.crs import from_epsg
from netCDF4 import Dataset

DATASET_ARCHIVE_LOCATION = '/share/appdata/qgreenland-private-archive/esa_cci_gravimetric_mass_balance_dtu/'
DATA_PATH = os.path.join(DATASET_ARCHIVE_LOCATION, 'greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820/CCI_GMB_GIS.nc')
OUTPUT_GPKG_PATH = os.path.join(DATASET_ARCHIVE_LOCATION, 'QGREENLAND_GEOPACKAGES')
DATE_FORMAT = '%Y_%m_%d_%H_%M_%S'

os.makedirs(OUTPUT_GPKG_PATH, exist_ok=True)

# Write out a simple README.
with open(os.path.join(OUTPUT_GPKG_PATH, 'README.txt'), 'w') as f:
    f.write(
        f'Geopackages generated from gmb_dtu_nc_to_gpkg.py on {dt.date.today():%Y-%m-%d}\n'
    )

ds = Dataset(DATA_PATH, 'r')
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
times = ds.variables['t'][:]
datas = ds.variables['GMB_trend'][:]
epoch_start = dt.datetime(2003, 1, 1)


def _schema_formatted_data(lat, lon, data, date_str):
    return {
        'geometry': {
            'type': 'Point',
            'coordinates': (lon, lat)
        },
        'properties': {
            'GMB_trend': data,
            't': date_str
        }
    }

gpkg_schema = {
    'geometry': 'Point',
    'properties': {
        'GMB_trend': 'float',
        't': 'str'
    }
}

crs = from_epsg(4326)

for time_idx, time in enumerate(times):
    date = epoch_start + dt.timedelta(days=float(time))
    date_str = date.strftime(DATE_FORMAT)
    with fiona.open(
            os.path.join(OUTPUT_GPKG_PATH, f'points_{date_str}.gpkg'),
            'w',
            crs=crs,
            driver='GPKG',
            schema=gpkg_schema) as f:
        for lat, lon, data in zip(lats, lons, datas[:, time_idx]):
            f.write(_schema_formatted_data(float(lat), float(lon), float(data), date_str))
