# Online layers reference

Some data layers may be best viewed from a service that provides data via an
internet connection (e.g., for data storage considerations). This document
provides a list of potentially useful services that QGIS can connect to to
provide layers via the internet.

See the [How to add an online layer to QGIS](/user-how-to/online-layers.md) page
for information on how to utilize these resources.

## Web Map Service (WMS)

* [Arctic Observing Viewer](https://arcticobservingviewer.org/web-services/)
  Observing Sites:
  `http://arcticgeoservices.org/arcgis/services/public/Arctic_Data_Collection_Sites/MapServer/WMSServer?request=GetCapabilities&service=WMS`

* [The National Snow and Ice Data Center
  (NSIDC)](https://nsidc.org/map-services/geospatial-map-services): `https://nsidc.org/api/mapservices/NSIDC/wms?version=1.1.0`

## Web Feature Service (WFS)

* [Arctic Observing Viewer](https://arcticobservingviewer.org/web-services/)
  Observing Sites:
  `http://arcticgeoservices.org/arcgis/services/public/Arctic_Data_Collection_Sites/MapServer/WFSServer?request=GetCapabilities&service=WFS`
  
* [Arctic Research Mapping Application](https://armap.org/web-services/)
  * Field Research Project Locations: `http://arcticgeoservices.org/arcgis/services/public/Arctic_Field_Research_Projects/MapServer/WFSServer`
  * Location Placenames: `http://arcticgeoservices.org/arcgis/services/public/Arctic_Field_Research_Site_Names/MapServer/WFSServer`
  * Arctic Countries: `http://arcticgeoservices.org/arcgis/services/public/Arctic_Countries/MapServer/WFSServer`
  * Arctic World Cities: `http://arcticgeoservices.org/arcgis/services/public/Places_World_Cities/MapServer/WFSServer`

* [The National Snow and Ice Data Center
  (NSIDC)](https://nsidc.org/map-services/geospatial-map-services): `https://nsidc.org/api/mapservices/NSIDC/wfs?version=1.1.0`

## Web Coverage Service (WCS)

* [The National Snow and Ice Data Center
  (NSIDC)](https://nsidc.org/map-services/geospatial-map-services): `https://nsidc.org/api/mapservices/NSIDC/wcs?version=1.1.0`
