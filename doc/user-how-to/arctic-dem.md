# Downloading Arctic DEM (100m) via the QGreenland Custom Plugin

As of version 2.0.0 of QGreenland Core, the Arctic DEM (100m) data layer has been removed from the 
QGreenland Core base package due to filesize. Now, this layer is available via the QGreenland Custom
QGIS plugin. To learn about how to install and configure the plugin, visit the 
[QGreenland Custom documentation](https://qgreenland-plugin.readthedocs.io/en/latest/)
on Read the Docs. This how-to will show you how to add the Arctic DEM (100m) layer to your QGIS project
using the QGreenland Custom plugin.

```{note}
The Polar Geospatial Center also provides a custom Greenland 32m resolution Arctic DEM for added detail.
To dowload this package, visit [qgreenland.org/download] and scroll to the Additional Data for QGreenland section.
```

First, open a project in QGIS and open the plugin window via the QGIS **Menu Bar**. 
You will see a set of directories of data layers underneath a search bar. 

![plugin_search](/_images/plugin_search.jpg)

To find the Arctic DEM, search 'DEM' in the search bar. Once located, click the checkbox next to the layer name. 
Next, you will need to choose a download location for this layer. Select a file location using the three-dot icon,
and when you are finished, click the Download button. Once the download is complete, you will see a blue 
progress bar showing the layer filesize. Click Next. 

![plugin_download](/_images/plugin_download.jpg)

Next, you will add the downloaded layer to your QGIS project. You will see a list of directories for data you have
downloaded using the plugin. If this is your first time using the plugin, the only directory you will see will be 
Terrain Models (parent directory for Arctic DEM). Click the checkbox next to Arctic DEM (100m) and click 
Add to Project, then click Close.

![add_to_project_plugin](/_images/add_to_project_plugin.jpg)

Now you have successfully used the QGreenland Custom plugin to download and add the Arctic DEM (100m) data layer to 
your QGIS project. Over in the QGIS **Layers Panel**, make sure the Arctic DEM (100m) layer is toggled on in order 
to see the layer in the **Map View**.

![arctic_dem](/_images/arctic_dem.jpg)