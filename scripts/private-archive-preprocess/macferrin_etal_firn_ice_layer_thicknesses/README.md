# Ice_Layer_Output_Thicknesses.csv

`Ice_Layer_Output_Thicknesses.csv` was obtained directly from Dropbox:
https://www.dropbox.com/home/2018_QArctic/Data%20suggestions/data%20sets.

To convert to a Geopackage:

```
ogr2ogr -oo X_POSSIBLE_NAMES=lon -oo Y_POSSIBLE_NAMES=lat -a_srs "EPSG:4326" -oo AUTODETECT_TYPE=True Ice_Layer_Output_Thicknesses.gpkg Ice_Layer_Output_Thicknesses.csv
```
