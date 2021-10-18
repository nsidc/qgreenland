import datetime as dt

from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


query_start_date = dt.date(1900, 1, 1)
query_end_date = dt.date(2021, 1, 1)

earthquakes = ConfigDataset(
    id='earthquakes',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[(
                'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?'
                f'starttime={query_start_date:%Y-%m-%d}%2000:00:00'
                f'&endtime={query_end_date:%Y-%m-%d}%2000:00:00'
                '&maxlatitude=90&minlatitude=51.179&maxlongitude=17.578'
                '&minlongitude=-103.359&minmagnitude=2.5&orderby=time'
            )],
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
