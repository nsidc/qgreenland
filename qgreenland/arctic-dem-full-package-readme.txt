-------------------
Getting Started:
-------------------

This package contains the 32m Arctic DEM and ancillary data:

* arcticdem_v4.1_32m_dem_greenland.vrt: 32-bit floating point elevation
  raster. This is the primary DEM tile datafile.

* arcticdem_v4.1_32m_browse_greenland.vrt: 32m DEM hillshade.

* arcticdem_v4.1_32m_datamask_greenland.vrt: Raster indicating DEM pixels with
  heights purely sourced from SETSM output (1) versus those that have been
  filled/merged with another dataset or mask out as NoData in quality control
  steps (0).

* arcticdem_v4.1_32m_count_greenland.vrt: Number of contributing DEMs.

* arcticdem_v4.1_32m_mad_greenland.vrt: Median absolute deviation of
  contributing DEMs.

* arcticdem_v4.1_32m_maxdate_greenland.vrt: Latest date of contributing DEMs in
  days since Jan 1, 2000.

* arcticdem_v4.1_32m_mindate_greenland.vrt: Earliest date of contributing DEMs
  in days since Jan 1, 2000.

Many small raster images (tiles) make up each of these layers to make a mosaic
of Greenland. To add this data to QGIS, navigate in the **Menu Bar** to **Layer
-> Add Layer -> Add Raster Layer** and browse to and select one of the included
.vrt files as the layer source. This .vrt file references all of the individual
tiles in the layer's associated `tiles/` subdirectory, and allows them all to be
loaded as a single mosaiced raster layer in QGIS. More information about VRTs
can be found here: https://gdal.org/drivers/raster/vrt.html.


-------------------
Building Overviews:
-------------------

Because each layer is large and consists of many smaller files, performance of
each layer after initially loading it into QGIS may be slow. We recommend that
users build raster overviews for each layer, which will increase the rendering
speed when zooming in/out.

To build overviews for a layer in QGIS, navigate in the **Menu Bar** to **Raster
-> Miscellaneous -> Build Overviews (Pyramids)** . Select the layer as the input
layer, and then click **Run** (leave the rest of the parameters as their
defaults). This process will take several minutes and produce a new `.ovr` file
in the data directory. The new `.ovr` file is expected to be several GB in size,
and there is no need to interact with this new file.


-------------------
Styling this data:
-------------------

For information on changing the symbology of raster layers in QGIS, see:

* QGIS lesson on changing raster symbology:
  https://docs.qgis.org/3.28/en/docs/training_manual/rasters/changing_symbology.html

* QGIS documentation on raster symbology properties:
  https://docs.qgis.org/3.28/en/docs/user_manual/working_with_raster/raster_properties.html#symbology-properties


-------------------
Citing this data:
-------------------

The ArcticDEM dataset should be cited as follows:

Porter, C., Howat, I., Noh, M.J., Husby, E., Khuvis, S., Danish, E., Tomko, K.,
Gardiner, J., Negrete, A., Yadav, B., Klassen, J., Kelleher, C., Cloutier, M.,
Bakker, J., Enos, J., Arnold, G., Bauer, G., and Morin, P., 2023, "ArcticDEM
- Mosaics, Version 4.1", https://doi.org/10.7910/DVN/3VDC4W
