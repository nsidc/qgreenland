import datetime as dt

from qgreenland.models.config.asset import ConfigDatasetCommandAsset
from qgreenland.models.config.dataset import ConfigDataset


query_start_date = dt.date(1900, 1, 1)
query_end_date = dt.date(2021, 1, 1)

def _lons():
    start_lon = 0

    while start_lon < 180:
        end_lon = start_lon + 2
        yield start_lon, end_lon
        yield -end_lon, -start_lon
        start_lon = end_lon



_args = [
    f'wget "https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime={query_start_date:%Y-%m-%d}%2000:00:00&endtime={query_end_date:%Y-%m-%d}%2000:00:00&maxlatitude=90&minlatitude=40&maxlongitude={end_lon}&minlongitude={start_lon}&minmagnitude=2.5&orderby=time" -O ' + '{output_dir}/' + f'earthquakes_{start_lon}_{end_lon}.geojson &&'
    for start_lon, end_lon in _lons()
]

# remove the last "&&"
_args[-1] = _args[-1].replace('&&', '')


earthquakes = ConfigDataset(
    id='earthquakes',
    assets=[
        ConfigDatasetCommandAsset(
            id='only',
            args=_args,
        ),
    ],
    metadata={
        'title': 'USGS Earthquakes 1990-2020',
        'abstract': (
            """United States Geological Survey earthquake data for earthquakes
            occuring during 1990-2020. Data is sourced from the ANSS
            Comprehensive Earthquake Catalog (ComCat). ComCat data are produced
            by contributing seismic networks."""
        ),
        'citation': {
            'text': (
                """U.S. Geological Survey (2020). ANSS Comprehensive Earthquake
                Catalog. Initial access: 2020-08-20."""
            ),
            'url': 'https://earthquake.usgs.gov/earthquakes/search/',
        },
    },
)
