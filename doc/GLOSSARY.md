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

A chain of steps to build a QGIS Layer.

## Step

A unit of work for transforming a layer. Must be a Linux shell command (e.g.
`gdalwarp` or `ogr2ogr`).
