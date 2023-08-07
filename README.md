<p align="center">
  <img alt="NSIDC logo" src="https://nsidc.org/themes/custom/nsidc/logo.svg" width="150" />
  <img alt="NSF logo" src="https://nsidc.org/sites/default/files/images/Logo/NSF.svg" width="150" />
</p>

[![NSF-1928393](https://img.shields.io/badge/NSF-1928393-red.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1928393)
[![DOI](https://zenodo.org/badge/241453043.svg)](https://zenodo.org/badge/latestdoi/241453043)

# QGreenland

![QGreenland example images](/doc/_images/qgreenland-examples.jpg)

[Our website](https://www.qgreenland.org) | [Documentation](https://qgreenland.readthedocs.io)

> :tada: QGreenland v3 development is well underway. We're looking for testers to
> provide feedback by **August 6, 2023**. Please see our
> [alpha release announcement](https://github.com/nsidc/qgreenland/discussions/694)
> for more details, including highlights of this release.


## A Free GIS package for Greenland

QGreenland is a free mapping tool to support interdisciplinary
Greenland-focused research, teaching, decision making, and collaboration.

Combines key datasets into a unified, all-in-one GIS analysis and visualization
environment for offline and online use.

An international Editorial Board and Project Collaborators connects the
QGreenland Team to data and user communities.


## Disclaimer

QGreenland should not be used as a sole navigational aid while performing
remote research activities in Greenland. Always bring appropriate safety and
navigational aids (including hard-copies of topographic maps) when visiting the
field.

QGreenland is a data-viewing and analysis platform, and the QGreenland Team does
not create new data. QGreenland's layers may contain errors from the original
data providers. QGreenland makes no guarantees about the accuracy and validity
of data contained in QGreenland. Limited notes on known data issues have been
added to the 'Populated places' layer metadata. Also, some layers may not
perfectly align with each other due to unidentified georeferencing issues with
the original data. We recommend using the 'Greenland coastlines 2017' layer as
the best approximation reference layer for geolocating Greenland's coastline.

Note that some data were transformed from their native data formats,
projections, and resolutions for inclusion within QGreenland. The included
metadata (>Layer Properties >Metadata >History) contains provenance information
on any transformations. All QGreenland GeoPackages and GeoTIFFs are projected
in `EPSG:3413`.


# Getting started

As of this writing, the oldest version of QGIS we support for the QGreenland release
series are:

* QGreenland `1.x`: QGIS `3.16.x LTR`
* QGreenland `2.x`: QGIS `3.16.x LTR`
* QGreenland `3.x`: QGIS `3.28.x LTR`

You can find downloads and instructions
[here](https://qgis.org/en/site/forusers/download.html).

After installing QGIS, [download QGreenland](https://qgreenland.org/download)
and unzip it with your unzip tool of choice if you haven not already done so.

> :warning: Ensure QGreenland is _actually_ unzipped; some operating systems will only
> "explore" a zip file when you double-click it without actually extracting it to disk.
> In Windows, please right-click and select `Extract all...`.

Finally double-click on (or use QGIS open) the `qgreenland.qgs` file that was just
extracted from the zip.


## What's inside the QGreenland Core zip package?

At the root of the zip file, you will find scientific discipline-specific directories
containing data (GeoTIFFs and GeoPackages). Additionally, the following files are
present at the package root:

* `UserGuide.pdf`: Detailed user-guide.
* `QuickStartGuide.pdf`: Guide for QGIS beginners.
* `README.html`: The README file you are currently reading.
* `CHANGELOG.html`: A summary of changes for each new QGreenland version.
* `layer_list.csv`: Comma-separated values representing the configuration of
  layers in QGreenland. This includes limited layer metadata, including, but not limited
  to: title, description, abstract, and citation.


# Educational resources

We keep the QGreenland official website up-to-date with links to helpful
educational resources, including our own QGreenland User Guide.

* [QGreenland official website](https://qgreenland.org)
* [QGreenland YouTube channel](https://www.youtube.com/channel/UCjWae_Jrbognx2ju_SHBZ2A/videos)
* [QGreenland official documentation](https://qgreenland.readthedocs.io)


# Contributing

Please see [contributing
instructions](https://qgreenland.readthedocs.io/en/latest/contributor-how-to/contribute-layers.html)
for more info. A good portion of this document contains technical instructions about
running the QGreenland pipeline, but also includes less-technical instructions for
contributing styles you have developed within QGIS. Our goal is to make it as easy as
possible for any user of QGreenland to contribute to the project, so please do not be
deterred from sharing your ideas.

**If all else fails, please [email us](mailto:qgreenland.info@gmail.com)!**


# Acknowledgements

Please see our
[acknowledgements](https://qgreenland.readthedocs.io/en/latest/acknowledgements.html)
for our best effort to acknowledge all of the giants upon whose shoulders we stand.
