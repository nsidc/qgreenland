# How to Locate Layer Metadata

Metadata refers to the general information about a data file, and the
metadata for QGreenland GIS data files can be accessed in two ways. 

```{note}
For more information on layer properties and metadata, see our Tutorial on
[Interacting with Geospatial Data in QGreenland
Core](/user/tutorials/interacting-with-geospatial-data.md).
```

## Via QGIS Layer Properties

If you have the QGreenland Core base package downloaded, you can easily locate
and view layer metadata within QGIS. First, open the **qgreenland.qgs** QGIS project file that was included
in the QGreenland Core download package. Next, locate your layer of interest in the **Layer Panel**.
The **Layer Panel** is a panel on the left side of the **Map View** containing a list of layers 
that are in your QGIS project.

![layer_panel_2.png](/_images/layer_panel_2.png)

Right click on the layer and select the **Properties** option. This will open the Layer Properties window.
Next, find the metadata tab on the left side window panel. This will show any available information
that is associated with the data layer, including but not limited to title and abstract.

![metadata.png](/_images/metadata.png)

## Via Text Files in Layer Directories

In each layer directory inside the QGreenland package, you should see 2 text
files, one **provenance.txt**, which includes information on how the data is
processed, and one **metadata.txt**.

Open up **metadata.txt** to read through the layer metadata including layer
description, dataset abstract, and citation information.

Open the **provenance.txt** file to see all of the processing steps applied to
the data for QGreenland.

![layer_dir.png](/_images/layer_dir.png)
