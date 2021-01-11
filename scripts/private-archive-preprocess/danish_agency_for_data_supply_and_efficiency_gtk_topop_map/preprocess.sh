#! /bin/bash

unzip GTK_TIFF_UTM24-WGS84.zip
cd gtk/G500/
gdalbuildvrt dms_gtk_topo.vrt *.tif
gdal_translate -co "COMPRESS=DEFLATE" -co "TILED=YES" dms_gtk_topo.vrt dms_gtk_topo.tif
gdal_edit.py -a_srs "EPSG:32624" dms_gtk_topo.tif
mv dms_gtk_topo.tif ../../
rm -rf gtk
