# How to Locate Layer Metadata

Metadata in GIS data refers to the general information about a data file, and the
metadata for QGreenland data files can be accessed via two ways. 

```{note}
Locating and viewing QGreenland layer metadata is easiest when you have already 
downloaded the QGreenland Core base package. You can download QGreenland Core
[here](https://qgreenland.org/download).
```

## Via the QGIS Attribute table

If you have the QGreenland Core base package downloaded, you can easily locate
and view layer metadata within QGIS. First, open the **qgreenland.qgs** file that was included
in the QGreenland Core download package. Next, locate your layer of interest in **Layer Panel**.
The **Layer Panel** is a panel on the left side of the **Map View** containing a list of layers 
that are in your QGIS project.

![layer_panel_2.png](/_images/layer_panel_2.png)

Then, right click on the layer and select the **Properties** option. This will open a window.
Next, find the metadata tab on the left side panel. This will show any available information
that is associate with the data layer, including but not limited to title, abstract, description,
etc.

![metadata.png](/_images/metadata.png)

## Using the QGreenland Custom plugin

If you have the QGreenland Custom QGIS plugin, you can access QGreenland layer metadata through the plugin.
First you will need download the layer of interest if you do not already have it downloaded. If you need help installing or downloading data using QGreenland Custom, please follow 
[this how-to guide](https://qgreenland-plugin.readthedocs.io/en/latest/user-how-to/plugin-how-to.html) first. 

Access the plugin via the **Web** tab in the top **Menu Bar**, and select the **Manage Data** option.
This will open a window showing any layers you have downloaded via the plugin. 

![add_to_project_plugin.png](/_images/add_to_project_plugin.png)

Click the **Explore files** button at the bottom left. This will open up a window to the download location
which you selected when downloading data via the plugin. If you have only downloaded 1 layer via the plugin,
you will only see 1 file directory here, otherwise, scroll through to find your layer of interest and open
up that directory. In the layer directory, you should see 2 text files, 1 **provenance.txt**, which includes
information on how the data was process, and 1 **metadata.txt**. Open up **metadata.txt**.

![layer_dir.png](/_images/layer_dir.png)