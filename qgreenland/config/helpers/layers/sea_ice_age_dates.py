import datetime as dt
from pathlib import Path

from cftime import num2pydate
from netCDF4 import Dataset
import pandas as pd


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
            week_str = f'{start_date:%B} {start_date:%d}-{end_date:%d}'
            return band_idx, week_str



if __name__ == '__main__':
    rankings_filepath = Path('/home/trst2284/Downloads/Sea_Ice_Index_Min_Max_Rankings_G02135_v3.0.xlsx')
    min_date, max_date = get_min_max_for_year(2010, rankings_filepath)

    print(get_band_of_date(
        Path('/share/appdata/qgreenland-input-cache/seaice_age.2010/iceage_nh_12.5km_20100101_20101231_v4.1.nc'),
        min_date,
    ))

    print(get_band_of_date(
        Path('/share/appdata/qgreenland-input-cache/seaice_age.2010/iceage_nh_12.5km_20100101_20101231_v4.1.nc'),
        max_date,
    ))
