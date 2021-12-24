# Get started with QGreenland

By completing this tutorial, the user will install QGIS, download and open the
QGreenland data package, become familiar with the QGIS interface, and browse
some data included in QGreenland.

## 1) Download and Install QGIS

Go to [qgis.org](https://qgis.org) and download the free QGIS software,
available on Windows, macOS, Linux and Android. It is recommended to download
the long term release (3.16 or later) version.

## 2) Download and open the QGreenland package

Download the QGreenland data package (v2.0.0) at
[https://qgreenland.org/download](https://qgreenland.org/download).

Save the zip package to a location of your choice and unzip it. Open the
`qgreenland.qgs` file in the data package folder by double-clicking it. QGIS
will open automatically and display the QGreenland data environment.


```{note}
Depending on your version of QGreenland, the package may be a `.qgs` or a
`.qgz` file. They should function the same as long as you have a compatible
version of QGIS.
```


```{note}
If QGIS is already open, one can open the `qgreenland.qgs` project file
within QGIS by navigating to the "Project >Open..." option in the menu bar and
selecting the `qgreenland.qgs` file from its saved location.
```


## 3) Get to know the QGIS Interface

The main components of the QGIS interface are the **Menu bar**, toolbars, panels,
**Map view**, and **Status bar**

![map_view](/_images/map_view.jpg)

The **Menu bar** and toolbars are different ways to access most QGIS functions, such
as opening or saving a project or analyzing the data using geoprocessing
tools. Panels are another way for users to interact with data layers and
functions in QGIS.

The **Layers panel** is where all data layers in the current project are
listed. Layers can be toggled on or off, which will control whether or not they
show up in the map view. Layers are listed in the order in which they show up in
the map view - layers at the top of the list show up on top in the map view, and
vice versa. Layers can be manually moved around in the layers panel to change
the order in which they show up. Panels and toolbars can also be manually moved
around the QGIS interface to fit the user’s preferences.

Lastly, the **Status bar** is the bar at the bottom of the QGIS window that shows
the current coordinate reference system of the map view, any available plugin
updates, and the map view scale. Also included in the **Status bar** is a quick
search bar and a button to open a **Log Messages** window to view log messages.


```{note}
The [QGIS User
Manual](https://docs.qgis.org/3.16/en/docs/user_manual/index.html) provides a
detailed and comprehensive overview of QGIS' core features. Users who are new to
Geographic Information Systems may also benefit from reviewing QGIS's [Gentle
Introduction to
GIS](https://docs.qgis.org/3.16/en/docs/gentle_gis_introduction/index.html)
```


## 4) Browse data in QGreenland

Layers in QGreenland are organized into groups by category. For example, the
"Background boundary" layer is "QGreenland boundaries" group, which is itself
inside of the "Reference" group ("Background boundary/Reference").

![layer_groups](/_images/layer_groups.jpg)

### Toggle layer visibility

Some layers are turned on by default when opening QGreenland. In order to
visualize another data layer (or remove an existing one), toggle the checkbox
next to the layer in the **Layers panel**.

Toggle on the "Ice thickness (150m)" layer, which is in the "Terrain
models/Bedmachine" group. The **Map view** should now include a visualization of
Ice thickness at a 150m spatial resolution.

![ice_thickness_displayed](/_images/ice_thickness_displayed.jpg)


```{note}
The search bar, located in the **Status bar**, can also be used to find layers
in the **Layers panel**.
![search_bar](/_images/search_bar.jpg)
```


### Navigate the Map View

The **Map view** can be interacted with using a combination of the mouse and the
**Map Navigation Toolbar**

![map_navigation_toolbar](/_images/map_navigation_toolbar.jpg)

By default, the **Pan Map** tool is selected
![pan_map](/_images/pan_map.jpg). This tool allows the user to click and drag on
the map view to change the extent. Try using this tool to pan around the map and
explore the geography surrounding Greenland.

The zoom tools ![zoom_in_out_icons](/_images/zoom_in_out_icons.jpg) can be used
to zoom in and out of the map view. Select the **Zoom In** tool and use it to
draw a box around southern Greenland to get a better look at the "Ice thickness
(150m)" layer in that part of Greenland. Now select the **Pan Map** tool again
and explore the layer in detail.

```{note}
The scroll wheel on your mouse or track pad can also be used to zoom in and out
in the **Map view**
```

Hovering over the other map navigation tool icons will provide a tool tip
indicating what the tool is used for. Try hovering over some of the other icons
in the **Map Navigation Toolbar** to read their tooltips. Try out some of these
other tools to explore the map and QGreenland's various data layers. See the
[QGIS documentation on zooming and
panning](https://docs.qgis.org/3.16/en/docs/user_manual/introduction/general_tools.html#zooming-and-panning)
for more detailed information on how to effectively navigate the **Map View**.


## 5) Summary

In completing this tutorial, the user has installed QGIS, downloaded and opened
the QGreenland data package, and learned about the fundamentals of using QGIS to
explore QGreenland. Having accomplished this, the user is prepared to explore
the many data layers included with QGreenland. The user is now ready to approach
more advanced topics such as performing geospatial analyses and preparing
publication-quality maps with the data in QGreenland.
