# greenland_SMB_database_v2020.xlsx

The source data can be acquired from: https://promice.org/PromiceDataPortal/api/download/1198f862-4afa-4862-952f-acd9129d790d/greenland_SMB_database_v2020/greenland_SMB_database_v2020.xlsx

## Preprocessing steps

Once data were acquired, the 'overview' sheet of the xlsx file was converted to
a 'locations.csv' csv file with `libreoffice`. The 'locations.csv' file was then
manually edited to remove records where the 'finished' column has a value of 'no
data found'.  The csv file was then converted to a geopackage via the following
`ogr2ogr` command:

```
ogr2ogr -oo X_POSSIBLE_NAMES=glacier_lon -oo Y_POSSIBLE_NAMES=glacier_lat -a_srs "EPSG:4326" -sql "select *, glacier_name as label from locations" locations.gpkg locations.csv`
```
