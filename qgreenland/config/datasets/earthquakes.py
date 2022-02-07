import datetime as dt

from qgreenland.models.config.asset import CommandAsset
from qgreenland.models.config.dataset import Dataset


query_start_date = dt.date(1900, 1, 1)
query_end_date = dt.date(2022, 1, 1)


_longitude_step = 2
# The USGS site seems to be rate limited. We'll get errors (name resolution
# error) if too much time is spent holding open connection(s) with the site.
# Faster downloads seem to work more reliably than slower ones. Do we need to do
# anything more, e.g. add sleeps to each `wget`, to give the server a break?
# TODO: What error was Trey getting?
wget_cmds = [
    (
        'wget \\"https://earthquake.usgs.gov/fdsnws/event/1/query.geojson'
        f'?starttime={query_start_date:%Y-%m-%d}%2000:00:00&endtime={query_end_date:%Y-%m-%d}%2000:00:00'
        f'&minlatitude=40&maxlatitude=90'
        f'&minlongitude={lon}&maxlongitude={lon + _longitude_step}'
        '&minmagnitude=2.5&orderby=time\\"'
        ' -O {output_dir}/' + f'earthquakes_{lon}_{lon + _longitude_step}.geojson'
    )
    for lon in range(-180, 180, _longitude_step)
]

wget_cmds_str = '\n'.join(wget_cmds)

earthquakes = Dataset(
    id='earthquakes',
    assets=[
        CommandAsset(
            id='only',
            # Use `xargs` to run lots of `wgets` in one asset.
            # TODO: Is this the best way to do multiple downloads for creating a
            # single layer?
            args=[
                'echo', f'"{wget_cmds_str}"',
                '|',
                'xargs',
                '-P', '2',
                '-d', '"\n"',
                '-I', 'QUERY', 'bash', '-c', '"QUERY"',
            ],
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
