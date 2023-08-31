-------------------
Getting Started:
-------------------

This package consists of many small raster images (tiles) which together make up
a larger 32m resolution Arctic DEM mosaic of Greenland. To add this data to
QGIS, navigate in the **Menu Bar** to **Layer -> Add Layer -> Add Raster Layer**
and browse to and select the included .vrt file as the layer source. This .vrt
file references all of the individual tiles in the `tiles/` subdirectory, and
allows them all to be loaded as a single mosaiced raster layer in QGIS. More
information about VRTs can be found here:
https://gdal.org/drivers/raster/vrt.html.


-------------------
Building Overviews:
-------------------

Because this dataset is large and consists of many smaller files, performance of
the layer after initially loading it into QGIS may be slow. We recommend that
users build raster overviews for this data, which will increase the rendering
speed when zooming in/out with the 32m Arctic DEM enabled.

To build overviews in QGIS, navigate in the **Menu Bar** to **Raster ->
Miscellaneous -> Build Overviews (Pyramids)** . Select the 32m Arctic DEM as the
input layer, and then click **Run** (leave the rest of the parameters as their
defaults). This process will take several minutes and produce a new `.ovr` file
in the data directory. The new `.ovr` file is expected to be ~5.5GB in size, and
there is no need to interact with this new file.


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

The ArcticDEM dataset should be cited as follows
Porter, C., Howat, I., Noh, M.J., Husby, E., Khuvis, S., Danish, E., Tomko, K.,
Gardiner, J., Negrete, A., Yadav, B., Klassen, J., Kelleher, C., Cloutier, M.,
Bakker, J., Enos, J., Arnold, G., Bauer, G., and Morin, P., 2023, "ArcticDEM
- Mosaics, Version 4.1", https://doi.org/10.7910/DVN/3VDC4W
