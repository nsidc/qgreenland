import datetime as dt
from pathlib import Path

import fiona
from fiona.crs import from_epsg
from netCDF4 import Dataset

PRIVATE_ARCHIVE_DIR = Path('/share/appdata/qgreenland-private-archive')
DATASET_ARCHIVE_LOCATION = PRIVATE_ARCHIVE_DIR / 'esa_cci_gravimetric_mass_balance_dtu/'
DATA_PATH = (
    DATASET_ARCHIVE_LOCATION
    / 'greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820'
    / 'CCI_GMB_GIS.nc'
)
OUTPUT_GPKG_PATH = DATASET_ARCHIVE_LOCATION / 'QGREENLAND_GEOPACKAGES'

OUTPUT_GPKG_PATH.mkdir(parents=True, exist_ok=True)

# Write out a simple README.
with open(OUTPUT_GPKG_PATH / 'README.txt', 'w') as f:
    f.write(
        'Geopackages generated from gmb_dtu_nc_to_gpkg.py on'
        f' {dt.date.today():%Y-%m-%d}\n',
    )

ds = Dataset(DATA_PATH, 'r')
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
times = ds.variables['t'][:]
start_times = ds.variables['start_time'][:]
end_times = ds.variables['end_time'][:]
datas = ds.variables['GMB_trend'][:]
epoch_start = dt.datetime(2003, 1, 1)


def _schema_formatted_data(lat, lon, data, *, start_date_str, end_date_str):
    return {
        'geometry': {
            'type': 'Point',
            'coordinates': (lon, lat),
        },
        'properties': {
            'GMB_trend': data,
            'start_date': start_date_str,
            'end_date': end_date_str,
        },
    }


gpkg_schema = {
    'geometry': 'Point',
    'properties': {
        'GMB_trend': 'float',
        'start_date': 'str',
        'end_date': 'str',
    },
}

crs = from_epsg(4326)

for idx, _ in enumerate(times):
    start_date = epoch_start + dt.timedelta(days=float(start_times[idx]))
    end_date = epoch_start + dt.timedelta(days=float(end_times[idx]))
    start_date_str = start_date.date().isoformat()
    end_date_str = end_date.date().isoformat()

    output_fp = OUTPUT_GPKG_PATH / f'points_{start_date_str}_{end_date_str}.gpkg'
    with fiona.open(
            output_fp,
            'w',
            crs=crs,
            driver='GPKG',
            schema=gpkg_schema) as f:
        for lat, lon, data in zip(lats, lons, datas[:, idx]):
            f.write(_schema_formatted_data(
                float(lat), float(lon), float(data),
                start_date_str=start_date_str,
                end_date_str=end_date_str,
            ))
