https://nsidc.slack.com/archives/CRB96FG68/p1608311238016100

# RACMO_QGreenland_Aug2020.zip

Original zipped package of data provided via Dropbox provided by Brice.

# extraced_1km.zip

Contains all of the uncompressed 1km .nc.gz files (`gunzip` ran
on the .nc.gz files to get .nc files). Our pipeline should be able to handle
this eventually.

Note that the `extracted_1km.zip` does not include the `refreeze` file, which
appears to have a problem (zero bytes). Attempts to `gunzip` this result in an
error:

```
gzip: refreeze.1958-2018.BN_RACMO2.3p2_FGRN055_1km.YYmean.nc.gz: unexpected end of file
```

# wind_vector_points.gpkg

`wind_vector_points.gpkg` contains points representing wind direction vectors derived
from the `u10m` and `v10m` component grids.

To generate this file, the `scripts/racmo_wind_vectors.py` script was used to create a `wind_vector_points.csv` file. Next, the following `ogr2ogr` command was used to convert the .csv to .gpkg:

```
ogr2ogr -oo X_POSSIBLE_NAMES=x -oo Y_POSSIBLE_NAMES=y -a_srs "EPSG:3413" -oo AUTODETECT_TYPE=True wind_vector_points.gpkg wind_vector_points.csv
```

The `wind_vector_points.csv` was then removed.
