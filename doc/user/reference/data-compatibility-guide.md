# Dataset Compatibility Guide

While QGreenland provides a curated base package of data on a variety of topics,
the options for adding additional data are nearly unlimited. We offer different
guidelines for data compatibility depending on what your goals are:

## Publishing previously unpublished data so it is compatible with QGreenland

To ensure that your own original research datasets will be easy to work with in
QGreenland, either in your own individual QGreenland project or as an addition
to the public QGreenland data package, please note the following:

   * Make sure your data are produced in a standard format with appropriate
     spatial metadata. For example, your dataset should have clearly defined
     projection metadata (as an EPSG code, proj4 params, OGC-compliant
     well-known-text, etc.) and should be formatted in a way that gdal/ogr tools
     can read and understand. Double check that your data can be opened in QGIS
     and appropriately geolocated.

   * If your data are not already in the QGreenland project coordinate reference
     system (EPSG:3413), that is OK. The QGreenland project includes all the
     tooling necessary to reproject your data, as long as the data meet the
     metadata requirements. A contributor to the QGreenland open source project
     can take it from here to ensure consistent and compatible results (see
     section 2 below).

   * Make sure your data are accompanied by metadata that describe the methods
     used for producing the data (e.g., scientific paper, document that
     describes the algorithm/data collection procedures used, etc.).

## Contributing datasets to QGreenland via GitHub for inclusion in future releases

Follow the instructions found in our {doc}`/contributor/discussion/contributing`
guidelines. The QGreenland source code defines “processing pipelines”, which, when
executed on a server or a user’s computer, fetch data from its original source location,
transform it (reproject, reformat, subset, resample, etc.) as needed, and finally
compile these data into a zipped QGreenland QGIS project. Contributors may customize,
re-use, or add to our processing pipelines to support their new layer, and when their
changes are ready, submit a [Pull
Request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
to contribute valuable changes back to the QGreenland project.

As of QGreenland v2.0.0, we support editing of dataset metadata, QGIS styles, and data
processing steps via simple Python-based configuration that is easy to learn. See the
{doc}`/contributor/reference/architecture/configuration` reference page for more
information.

   * Ensure that all outputs of QGreenland processing pipelines are in EPSG:3413
     coordinate reference system.

   * Ensure that all outputs of the QGreenland processing pipelines are in the
     correct format. We expect one GeoPackage per vector layer and one GeoTIFF
     per raster layer.

   * Fill out all metadata as configuration. This includes abstract, citation,
     layer description and title, etc. The QGreenland processing pipelines will
     automatically format this information and add it to the correct interfaces
     (metadata tab) in QGIS.

##  Adding datasets to your QGreenland project for personal use only

   * Refer to our documentation page on [Adding New Datasets to
     QGreenland](/user/how-to/adding-data.md) for instructions on how to add new
     data layers to your QGreenland project. Note that this section is also
     incldued in the `UserGuide.pdf` included in the QGreenland Core package.

   * Note that the QGreenland data package is in the EPSG:3413 coordinate
     reference system and all pre-loaded layers are either GeoTIFF (raster) or
     GeoPackage (vector) files.
