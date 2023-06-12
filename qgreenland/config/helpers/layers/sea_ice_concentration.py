import calendar

from qgreenland.models.config.asset import HttpAsset

CONCENTRATION_START_YEAR = 2011
CONCENTRATION_END_YEAR = 2022
MAX_CONCENTRATION_YEARS = range(CONCENTRATION_START_YEAR, CONCENTRATION_END_YEAR + 1)
MIN_CONCENTRATION_YEARS = range(CONCENTRATION_START_YEAR, CONCENTRATION_END_YEAR + 1)
CONCENTRATION_DESCRIPTION = """Monthly average of sea ice concentration as a percentage (e.g., 99.9 =
    99.9%). Values under 15% are considered to be open water."""
CONCENTRATION_STYLE = "sea_ice_concentration"

# Off-years are years where the maximum occurs in a month other than March. This
# mapping defines years which are off-years and which month the maximum occurred
# in that year.
CONC_MAX_OFF_YEARS: dict[int, int] = {
    2015: 2,  # Max day was 2015-02-25
    2022: 2,  # Max day was 2022-02-25
}


def conc_max_month(year: int) -> int:
    """Return the month in which the concentration maximum occurred."""
    return CONC_MAX_OFF_YEARS.get(year, 3)


def concentration_maximum_asset_for_year(year: int) -> HttpAsset:
    """Handle the maximum concentration "off-years"."""
    month = conc_max_month(year)
    month_abbr = calendar.month_abbr[month]

    return HttpAsset(
        id=f"maximum_concentration_{year}",
        urls=[
            (
                "ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/geotiff"
                f"/{month:02d}_{month_abbr}/N_{year}{month:02d}_concentration_v3.0.tif"
            )
        ],
    )
