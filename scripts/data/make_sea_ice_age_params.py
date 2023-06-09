"""Generate sea ice age parameters file.

Must be executed when the sea ice age dataset is updated. Ensure you've fetched
the data first, as that is read as input to this script:

    ./scripts/cli.sh fetch seaice_age

Save the output by running the following from the repo root:

```
OUT_PATH=$PWD/qgreenland/config/helpers/ancillary/sea_ice_age_params.json
docker exec luigi \
python /luigi/tasks/qgreenland/scripts/data/make_sea_ice_age_params.py > $OUT_PATH
```
"""
import datetime as dt
import functools
import json
import tempfile
from pathlib import Path

import pandas as pd
import requests
from cftime import num2pydate
from netCDF4 import Dataset

from qgreenland.config.datasets.seaice import seaice_age as dataset
from qgreenland.constants.paths import FETCH_DATASETS_DIR


@functools.cache
def _get_min_max_rankings_file() -> bytes:
    """Fetch the Sea Ice Index Min/Max rankings spreadsheet and return its content."""
    response = requests.get(
        "https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/"
        "seaice_analysis/Sea_Ice_Index_Min_Max_Rankings_G02135_v3.0.xlsx"
    )

    return response.content


def get_min_max_dates_for_year(year: int) -> tuple[dt.date, dt.date]:
    """Return dates of the min and max sea ice extent for a given year."""
    with tempfile.NamedTemporaryFile() as tmpf:
        tmpf.write(_get_min_max_rankings_file())

        ds = pd.read_excel(
            tmpf.name,
            sheet_name="NH-Annual-5-Day-Extent",
            index_col=0,  # Index by year (unlabeled)
        )

    date_format = "%Y-%m-%d"
    min_date = dt.datetime.strptime(ds.loc[year]["min-date"], date_format).date()
    max_date = dt.datetime.strptime(ds.loc[year]["max-date"], date_format).date()

    return min_date, max_date


def get_band_info_for_date(target_date: dt.date) -> tuple[int, str]:
    """Return the band index and a descriptive text for the layer title."""

    def _get_data_fp_from_cache(year: int) -> Path:
        filepath = (
            FETCH_DATASETS_DIR
            / f"seaice_age.{year}"
            / f"iceage_nh_12.5km_{year}0101_{year}1231_v4.1.nc"
        )

        if not filepath.is_file():
            raise FileNotFoundError(f"Expected file {filepath} does not exist.")

        return filepath

    data_filepath = _get_data_fp_from_cache(target_date.year)
    ds = Dataset(data_filepath)
    time = ds.variables["time"]

    band_dates = [
        real_date.date() for real_date in num2pydate(time[:], units=time.units)
    ]

    for band_idx, start_date in enumerate(band_dates, start=1):
        end_date = start_date + dt.timedelta(days=6)

        if start_date <= target_date and target_date <= end_date:
            if start_date.month == end_date.month:
                week_str = f"{start_date:%B} {start_date:%-d}-{end_date:%-d}"
            else:
                week_str = (
                    f"{start_date:%B} {start_date:%-d}-{end_date:%B}{end_date:%-d}"
                )

            return band_idx, week_str

    raise RuntimeError("Failed to find data matching target_date.")


def make_seaice_age_layers_params() -> None:
    """Write sea_ice_age_params.json.

    sea_ice_age_params.json contains params for each layer by year.
    """
    layers_params = {}
    dataset_years = [int(year_str) for year_str in dataset.assets.keys()]
    for year in dataset_years:
        min_date, max_date = get_min_max_dates_for_year(year)

        min_band, min_week_str = get_band_info_for_date(min_date)
        max_band, max_week_str = get_band_info_for_date(max_date)

        layers_params[year] = {
            "minimum": {
                "date_range": min_week_str,
                "band_num": min_band,
            },
            "maximum": {
                "date_range": max_week_str,
                "band_num": max_band,
            },
        }

    print(
        json.dumps(
            layers_params,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    make_seaice_age_layers_params()
