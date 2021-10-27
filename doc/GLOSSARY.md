# End-user

Someone who uses QGreenland in QGIS.


## Boundary

Instead of extent, which to some may imply rectangular or lon/lat-based shape,
use the term "Boundary".

You can define as many boundaries as you want with arbitrary names, in addition
to the required `data` boundary, which is used for defining the initial extent
shown when opening QGIS.


# Pipeline Contributor

Someone who adds more layers to QGreenland by configuring pipeline(s) to
transform source data in to a standard QGreenland specification.


## Pipeline

A chain of steps to build a QGIS Layer.

## Step

A unit of work for transforming a layer. Must be a Linux shell command (e.g.
`gdalwarp` or `ogr2ogr`).
