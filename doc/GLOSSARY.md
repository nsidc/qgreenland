# End-user

Someone who uses QGreenland in QGIS.


## Boundary

Instead of extent, which to some may imply rectangular or lon/lat-based shape,
use the term "Boundary".

TODO: Data boundary, background boundary are confusing terms. Some data is
subset to the background boundary. Need better words.


# Pipeline Contributor

Someone who adds more layers to QGreenland by configuring pipeline(s) to
transform source data in to a standard QGreenland specification.


## Pipeline

A chain of steps to build a QGIS Layer. Pipeline contributors generally create
these using YAML (TODO: Link to YAML "About" page) to define steps as GDAL/OGR
commands.


## Step

A unit of work for transforming a layer. Can be a Python method, a Linux shell
command (e.g. `gdal` or `ogr2ogr`), or even a templated collection of other
steps.
