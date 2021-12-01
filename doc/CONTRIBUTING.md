This project is currently undergoing rapid development, so expect change in any
release except releases labeled as "stable". Stable releases can be found at
[https://qgreenland.org/explore](https://qgreenland.org/explore)!


# The processing pipeline

In general, a data-processing pipeline looks like this:

* Fetch input assets
* Run layer pipelines, writing outputs to final layer hosting locations.
* For layers for which `in_package` is `True`, use hardlinks to link final
  layer ouputs to a QGreenland package compile location.
* Create QGreenland package QGIS project file and other ancillary package
  files.
* Zip the QGreenland package.


# Contributing to the project

One of the primary goals of this project is to allow for scientists comfortable
with standard GIS command-line tools to contribute new layers with as little
friction as possible.

Contributing new datasets and layers requires writing simple Python objects
containing the relevant data (metadata, download location, transformation
steps) needed to include the layer in QGreenland.

Currently, layer styles can be contributed without any programming knowledge by
designing the style in QGIS, saving it as a `.qml`, and committing it to the
`qgreenland/ancillary/styles` directory.

You can contribute to this project even if you don't have write access by
forking, making your change, making all CI checks pass, then opening a Pull
Request. Learn more:

https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork


## How-tos

* [How to run QGreenland](/doc/how-to/RUN_QGREENLAND.md)
* [How to contribute styles](/doc/how-to/CONTRIBUTE_STYLES.md)
* [How to contribute new layers](/doc/how-to/CONTRIBUTE_NEW_LAYERS.md)
* [How to release a new version of Qgreenland code](/doc/how-to/RELEASE_NEW_VERSION.md)
