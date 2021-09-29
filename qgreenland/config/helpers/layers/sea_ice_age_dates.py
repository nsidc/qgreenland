import datetime as dt

from cftime import num2date
from netCDF4 import Dataset
import pandas as pd


def get_min_max_for_year(year: int, rankings_filepath: str) -> tuple[dt.date, dt.date]:
    ds = pd.read_excel(
        rankings_filepath,
        sheet_name='NH-Annual-5-Day-Extent',
        index_col=0,  # Index by year (unlabeled)
    )

    date_format = '%Y-%m-%d'
    min_date = dt.datetime.strptime(ds.loc[year]['min-date'], date_format).date()
    max_date = dt.datetime.strptime(ds.loc[year]['max-date'], date_format).date()

    return min_date, max_date


def get_band_of_date(data_filepath: str, target_date: dt.date):
    ds = Dataset(data_filepath)
    time = ds.variables['time']

    band_dates = num2date(time[:], units=time.units, caledndar=time.calendar)

    for band_idx, start_date in enumerate(band_dates, start=1):
        end_date = start_date + dt.timedelta(days=6)

        if start_date <= target_date and target_date <= end_date:
            week_str = f'{start_date:%B} {start_date:%d}-{end_date:%d}'
            return band_idx, week_str
