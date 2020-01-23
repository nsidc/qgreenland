# Greenland-spike

This project uses `luigi` pipelines to generate the QGreenland package.

## Pipelines

After each dataproduct pipeline (enumerated below) is run, the project is compiled:

* Generate .qgs/.qgz project file including all dataproducts
* Zip it -- zip it good

### Shapefiles

* Unzip (optional)
* Reproject( EPSG:3411 )
* Subset( QGreenland extent )
