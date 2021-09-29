import datetime as dt
import json
from pathlib import Path

from cftime import num2pydate
from netCDF4 import Dataset
import pandas as pd

from qgreenland.constants import CONFIG_DIR, INPUT_DIR


def get_min_max_for_year(year: int, rankings_filepath: Path) -> tuple[dt.date, dt.date]:
    ds = pd.read_excel(
        rankings_filepath,
        sheet_name='NH-Annual-5-Day-Extent',
        index_col=0,  # Index by year (unlabeled)
    )

    date_format = '%Y-%m-%d'
    min_date = dt.datetime.strptime(ds.loc[year]['min-date'], date_format).date()
    max_date = dt.datetime.strptime(ds.loc[year]['max-date'], date_format).date()

    return min_date, max_date


def get_band_of_date(data_filepath: Path, target_date: dt.date):
    ds = Dataset(data_filepath)
    time = ds.variables['time']

    band_dates = [real_date.date() for real_date in num2pydate(time[:], units=time.units)]

    for band_idx, start_date in enumerate(band_dates, start=1):
        end_date = start_date + dt.timedelta(days=6)

        if start_date <= target_date and target_date <= end_date:
            if start_date.month == end_date.month:
                week_str = f'{start_date:%B} {start_date:%d}-{end_date:%d}'
            else:
                week_str = f'{start_date:%B} {start_date:%d}-{end_date:%B}{end_date:%d}'
                
            return band_idx, week_str


def make_seaice_age_layers_cfg(start_year, end_year):
    rankings_filepath = Path('/home/trst2284/Downloads/Sea_Ice_Index_Min_Max_Rankings_G02135_v3.0.xlsx')

    def _get_data_from_cache(year):
        # filepath = INPUT_DIR / f'seaice_age.{year}' / f'iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc'
        filepath = Path('/share/appdata/qgreenland-input-cache/') / f'seaice_age.{year}/iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc'

        if not filepath.is_file():
            raise FileNotFoundError(f'Expected file {filepath} does not exist.')

        return filepath

    layers_cfg = {}
    for year in range(start_year, end_year + 1):
        min_date, max_date = get_min_max_for_year(year, rankings_filepath)
        data_filepath = _get_data_from_cache(year)

        min_band, min_week_str = get_band_of_date(data_filepath, min_date)
        max_band, max_week_str = get_band_of_date(data_filepath, max_date)

        layers_cfg[year] = {
            'minimum': {
                'date_range': min_week_str,
                'band_num': min_band,
            },
            'maximum': {
                'date_range': max_week_str,
                'band_num': max_band,
            },
        }

    return layers_cfg


if __name__ == '__main__':
    layers_cfg = make_seaice_age_layers_cfg(2010, 2019)
    with open(CONFIG_DIR / 'helpers/layers/sea_ice_age_cfg.json', 'w') as f:
        f.write(json.dumps(layers_cfg))
