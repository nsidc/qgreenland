# v0.9.0 (2020-02-18)

* Add QGreenland logo and copyright text as QGIS decorations at bottom-left.

# v0.8.0 (2020-02-12)

* Pre-compute statistics for raster layers so that QGIS can render those layers
  with the correct min/max values.

# v0.7.0 (2020-02-11)

* Add task to generate overviews for raster layers.
  * Generate overviews for Arctic DEM layer.

* Add VM configuration and update README on how to use VM to run tasks and serve
  data.

# v0.6.0 (2020-02-07)

* Add citations to each layer as tooltips. We're currently not sure how to
  populate the actual "Abstract" field in the metadata tab in QGIS using
  pyqgis.

# v0.5.0 (2020-02-07)

* Add config option for gdal warp arguments
  * Downsample BedMachine to 1km

# v0.4.0 (2020-02-07)

* New layer: IceBridge BedMachine

# v0.3.0 (2020-02-06)

* Added hillshade style to Arctic DEM layer.

# v0.2.0 (2020-02-05)

* New layer: Arctic DEM

# v0.1.0 (2020-01-23)

* New layer: Coastlines
