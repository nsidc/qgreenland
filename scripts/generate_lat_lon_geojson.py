import os
import math

import geopandas
import numpy
import pandas as pd
from shapely.geometry import LineString

OUT_DIR = './out'
degrees_template = '{deg}° {min}\' {sec}"'


def _decimal_degrees_to_dms(decimal, *, lat_or_lon, include_secs=True):
    """Convert decimal degrees to degrees, minutes, seconds.

    There are 60 minutes in a degree, and 60 seconds in a minute.
    """
    if lat_or_lon == 'lat':
        cardinal = 'S' if decimal < 0 else 'N'
    elif lat_or_lon == 'lon':
        cardinal = 'W' if decimal < 0 else 'E'
    else:
        raise RuntimeError(f"{lat_or_lon} is not 'lat' or 'lon'")

    degs = math.floor(decimal)

    mins_decimal = (decimal - math.floor(decimal)) * 60
    mins = math.floor(mins_decimal)

    secs = (mins_decimal - math.floor(mins_decimal)) * 60

    if include_secs is True:
        return f"{degs}° {mins}' {secs}\" {cardinal}"
    else:
        return f"{degs}° {mins}' {cardinal}"


def latitudes(*, increment=1):
    """Create a GeoDataFrame of latitudes at the given increment.

    increment: decimal degrees
    """
    RANGE = (0, 90)
    lats = []

    for lat in numpy.arange(RANGE[0], RANGE[1], increment):
        lats.append({
            'wgs84Degrees': _decimal_degrees_to_dms(lat, lat_or_lon='lat'),
            'wgs84Decimal': float(lat),
            'label': _decimal_degrees_to_dms(
                lat, lat_or_lon='lat', include_secs=False
            ),
            'geometry': LineString([(-180, lat), (180, lat)]),
        })

    return geopandas.GeoDataFrame(lats)


def longitudes(*, increment=1):
    """Create a GeoDataFrame of longitudes at the given increment.

    increment: decimal degrees
    """
    RANGE = (-180, 180)
    lons = []

    for lon in numpy.arange(RANGE[0], RANGE[1], increment):
        lons.append({
            'wgs84Degrees': _decimal_degrees_to_dms(lon, lat_or_lon='lon'),
            'wgs84Decimal': float(lon),
            'label': _decimal_degrees_to_dms(
                lon, lat_or_lon='lon', include_secs=False
            ),
            'geometry': LineString([(lon, -90), (lon, 90)]),
        })

    return geopandas.GeoDataFrame(lons)


def write_geojson(generator, **kwargs):
    """Write a GeoJSON file with the data returned by generator(**kwargs)."""
    lat_or_lon = generator.__name__
    increment_str = str(kwargs['increment']).replace('.', '_')

    fn = f'{lat_or_lon}_{increment_str}_degree.geojson'

    gdf = generator(**kwargs)
    gdf.to_file(os.path.join(OUT_DIR, fn), driver='GeoJSON')


def main():
    os.makedirs(OUT_DIR)

    # Generate latitudes and longitudes with exactly the same increments as
    # Quantarctica
    for increment in [0.25, 0.5, 1, 2, 5, 10, 15, 20, 30]:
        write_geojson(latitudes, increment=increment)
    for increment in [0.5, 1, 2, 3, 5, 10, 15, 20, 30, 45, 90]:
        write_geojson(longitudes, increment=increment)


if __name__ == '__main__':
    main()
    print(f'Outputs created at: {os.path.abspath(OUT_DIR)}')
