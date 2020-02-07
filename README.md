# Greenland-spike

This project uses `luigi` pipelines to generate the QGreenland package.


## Credentials

In order to download data behind Earthdata Login, you must provide the following environment variables:

* `EARTHDATA_USERNAME`
* `EARTHDATA_PASSWORD`

The correct values can be found in Vault at the path `nsidc/apps/qgreenland`.


## Pipelines

After each dataproduct pipeline (enumerated below) is run, the project is compiled:

* Generate .qgs/.qgz project file including all dataproducts
* Zip it -- zip it good


### Shapefiles

* Unzip (optional)
* Reproject( EPSG:3411 )
* Subset( QGreenland extent )
