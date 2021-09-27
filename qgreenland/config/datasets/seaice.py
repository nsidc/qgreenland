from qgreenland.config.helpers.layers.sea_ice_concentration import (
    CONCENTRATION_YEARS,
    concentration_maximum_asset_for_year,
)
from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


seaice_index = ConfigDataset(
    id='seaice_index',
    assets=[
        *[
            ConfigDatasetHttpAsset(
                id=f'median_extent_line_{month:02d}',
                urls=[(
                    'ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/shapefiles/shp_median'
                    f'/median_extent_N_{month:02d}_1981-2010_polyline_v3.0.zip'
                )],
            ) for month in range(1, 12 + 1)
        ],
        *[
            ConfigDatasetHttpAsset(
                id=f'minimum_concentration_{year}',
                urls=[(
                    'ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/geotiff'
                    f'/09_Sep/N_{year}09_concentration_v3.0.tif'
                )],
            ) for year in CONCENTRATION_YEARS
        ],
        *[
            concentration_maximum_asset_for_year(year) for year in CONCENTRATION_YEARS
        ],
    ],
    metadata={
        'title': 'Sea Ice Index, Version 3',
        'abstract': (
            """The Sea Ice Index provides a quick look at Arctic- and
            Antarctic-wide changes in sea ice. It is a source for consistent,
            up-to-date sea ice extent and concentration images, in PNG format,
            and data values, in GeoTIFF and ASCII text files, from November 1978
            to the present. Sea Ice Index images also depict trends and
            anomalies in ice cover calculated using a 30-year reference period
            of 1981 through 2010.
            The images and data are produced in a consistent way that makes the
            Index time-series appropriate for use when looking at long-term
            trends in sea ice cover. Both monthly and daily products are
            available. However, monthly products are better to use for long-term
            trend analysis because errors in the daily product tend to be
            averaged out in the monthly product and because day-to-day
            variations are often the result of short-term weather."""
        ),
        'citation': {
            'text': (
                """Fetterer, F., K. Knowles, W. N. Meier, M. Savoie, and A. K.
                Windnagel. 2017, updated daily. Sea Ice Index, Version 3.
                Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center.
                doi: https://doi.org/10.7265/N5K072F8. 2020-08-06."""
            ),
            'url': 'https://nsidc.org/data/g02135',
        },
    },
)
