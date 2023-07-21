# How to add an online layer to QGIS

When access to the internet is available, QGIS is capable of connecting to
various online map services that can provide access to additional geospatial
data that compliments QGreenland. Common map services include:

* [Web Map Service (WMS)](https://www.ogc.org/standards/wms): Provides image
  representations of geospatial data.
* [Web Coverage Service (WCS)](https://www.ogc.org/standards/wcs): Provides
  access to raster data
* [Web Feature Service (WFS)](https://www.ogc.org/standards/wfs): Provides
  access to vector data

This how-to guide covers creating a new connection to a WMS and adding a layer
from that service. WCS, WFS, and other online services can be interacted with in
a similar way.

For more information about adding online layers, see the following resources
from QGIS:

* [Online resources tutorial](https://docs.qgis.org/3.16/en/docs/training_manual/online_resources/index.html)
* [OGC web services user manual](https://docs.qgis.org/3.16/en/docs/user_manual/working_with_ogc/ogc_client_support.html)


## Add a WMS Layer

First, open the “Data Source Manager” from the top **Menu Bar** **(Layer >Data Source
Manager)** and select the “WMS/WMTS” option.

![wms_data_management_screen](/_images/wms_data_management_screen.jpg)

Click “New” to add a new connection to a WMS server. In this example, we will be
using the National Snow and Ice Data Center’s (NSIDC). Add a descriptive name
(e.g., ‘NSIDC’) and add the following URL to the “URL” field:
`https://nsidc.org/api/mapservices/NSIDC/wms?version=1.1.0.`

```{note}
Additional
information about NSIDC’s web map services is available here:
[https://nsidc.org/map-services/geospatial-map-services](https://nsidc.org/map-services/geospatial-map-services).

For additional online resources, see the [Online layers
reference](/user/reference/online-resources.md) page.
```

![wms_connection_details](/_images/wms_connection_details.png)

Click “OK”. This will create and select a new server connection to NSIDC’s WMS
that can be re-used between sessions of QGIS.

Click “Connect”. This will populate a list of available layers for the currently
selected server.

![wms_layer_listing](/_images/wms_layer_listing.jpg)

Use the search bar or scroll to the
`nsidc_0478_v2_measures_greenland_ice_sheet_vel` layer and select it. This layer
provides a visualization of Greenland ice sheet velocity. See NSIDC’s
documentation for this dataset for more information:
[https://nsidc.org/data/nsidc-0478](https://nsidc.org/data/nsidc-0478).

Finally, click “Add”. The layer will be added to the **Layers Panel** in QGIS.

![wms_layer_added](/_images/wms_layer_added.jpg)


```{warning}
The added layer will be inserted below whatever layer was previously selected in
the **Layers Panel**. This may mean that the layer is covered by other layers above
it. If the layer does not show up within a few seconds, check which layers are
above the inserted layer and reorder as needed.
```

```{note}
Some online layers are a timeseries. QGIS will automatically detect layers
with a time component and identify them as such with a clock icon next to the
layer name in the **Layers Panel**.

![timeseries_layer_clock_icon](/_images/timeseries_layer_clock_icon.png)

**Temporal Layers** can be interacted with using the Temporal Controller. See the
[qgistutorials.com](https://www.qgistutorials.com/en/docs/3/animating_time_series.html)
tutorial on animating timeseries data for more information on how to use the
Temporal Controller.
```
