# Eva placenames preprocessing steps

## 20201112_Oqaasileriffik_place-name register.zip

Provided by Eva. This data was placed in the appropriate private archive location and then unzipped:

```
cd /share/appdata/qgreenland-private-archive/eva_placenames
unzip 20201112_Oqaasileriffik_place-name register.zip
```


## 2021 0119_Oqaasileriffik_place-name categories_ENG.xlsx

Provided by Arnaq B. Johansen via email on Jan 19, 2021.

This file was placed in the appropriate private archive location and then
manually converted to a .csv using libreoffice.

## Run `preprocess.py`

Finally, run the `preprocess.py` script to join the translations with the
geospatial data and save as a geopackage that gets used in QGreenland.
