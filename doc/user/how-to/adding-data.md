# Adding New Datasets to QGreenland

Once the QGreenland Core package is downloaded and extracted onto a user’s
computer, it is fully customizable by the user. One can add new data, delete
layers within QGreenland, or make changes.  Saving the project will update the
qgreenland.qgs project file. If you do not want to overwrite the original project
version, simply save your updated project using a new filename via ‘Save As...’
You can create as many different projects as you like, adding or removing data
from the downloaded QGreenland package or adding data from elsewhere on your
computer.

## Adding New Layers in QGIS

To add new data layers to QGreenland in QGIS:
1. In the **Menu Bar**, go to **Layer -> Add Layer**, and choose the layer type
   you want to add. Alternatively, you can either click on the desired add layer
   button in the toolbar, or click on the **Data Source Manager** button in the
   **Data Source Manager** toolbar.
2. Any option you choose will open the same **Data Source Manager** window. On
   the right side of the window, you can double check that the layer type you want
   to add is highlighted.
3. Navigate to the data file that you want to add as a layer, then click **Add**.

To learn about adding online-access layers (e.g, WMS, WFS, WCS), see our
documentaiton on [How to add an online layer to
QGIS](/user/how-to/online-layers.md)!


## Selecting for Greenland-Specific Vector Data

Because the geographic extent of some QGreenland data layers extends beyond the
geographic and political border of Greenland to include the surrounding water bodies
and land masses, it might sometimes be necessary to filter out certain data if one is only
interested in data within Greenland’s geographic boundary. You can do this using the
"Greenland coastlines 2017" polygon layer.

To filter for data inside of Greenland:
1. Make sure that the group you want the filtered/extracted data to be added to is
   selected/highlighted in the **Layers Panel**.
2. Open the **Processing Toolbox** and go to **Vector selection -> Extract by location**.
3. Fill in the following parameters:
   * Extract features from = the data layer you want to filter, for example, Ice cores
   * Where the features (geometric predicate) = are within (you can also check intersect and
     others to capture data that might be located along the Greenland coastline)
   * By comparing to the features from = Greenland coastlines 2017
   * Extracted (location) = You can either save the file output from this as a temporary layer
     or as a permanent layer somewhere on your computer or within your QGreenland data
     package. Note: If you try to save the file as a GeoPackage layer (GPKG) and receive an
     error, try again and save it as a Shapefile (SHP) instead.
4. Click **Run** and close the window.

The filtered data will show up in the **Layers Panel** within the group you had selected and likely
named **Extracted (location)**. You can rename the layer by right clicking on it and selecting
**Rename Layer**.

## Editing Vector Data Layers
How do you add or delete points, line segments, or polygons to/in an existing vector layer in
your QGreenland project?

To edit a vector layer:
1. Select the layer you want to edit in the **Layers Panel** (click on it so that it is
   highlighted).
2. Toggle into editing mode by either right clicking on the vector layer you are
   editing in the **Layers Panel** and selecting **Toggle Editing** or by clicking on the
   **Toggle Editing** button in the **Digitizing** toolbar.
3. With **Editing** on, you will have access to new editing buttons in the **Digitizing**
   toolbar:
   * **Add new points to a point vector layer**
   * **Add new lines to a line vector layer**
   * **Add new polygons to a polygon vector layer**
4. Whenever you create any new vector feature, you will be prompted to enter
   attribute information for the new feature for its record in the layer’s **Attribute
   Table**.
5. If you just want to edit a record in a vector layer’s **Attribute Table**, you can open
   the **Attribute Table** and click on the **Toggle Editing** icon in the table toolbar. Be
   sure to save the layer edits after you are done making edits.
6. When you’re finished, click on the **Toggle Editing** button again in the toolbar to
   disable editing.

## Creating New Vector Layers from Scratch

In your QGreenland project, you may want to create a new vector layer from
scratch, such as a point layer of potential study sites for for your research in
Greenland.

To draw a new vector layer from scratch, use the **Layer -> Create Layer** menu
and select one of the following options:

* New GeoPackage Layer (reccomended)
* New Shapefile Layer (not reccomended, see
  [switchfromshapefile.org](http://switchfromshapefile.org/)).
* New Spatiallite Layer
* New Temporary Scratch Layer (will not persist data to disk!)

In the new window that opens after selecting one of these options, fill out the
given options (each will be slightly different). For detailed instructions on
how to add vector layers, see the [QGIS
documentation](https://docs.qgis.org/3.28/en/docs/user_manual/managing_data_source/create_layers.html#creating-new-vector-layers).


### Creating a GeoPackage layer

1. In the **Menu Bar**, go to **Layer -> Create Layer -> New GeoPackage Layer**
   or click on the **New GeoPackage Layer** button in the **Data Source
   Manager** toolbar.
2. A [GeoPackage](http://www.geopackage.org/) is a GIS file format that allows
   you to save multiple layers in one file; thus, you will actually be creating
   a new GeoPackage database that your new GeoPackage layer will live in. In the
   new window:
   * Name your new Database
   * Name the new GeoPackage layer you are creating - this is the **Table name**
   * Specify the geometry of the new GeoPackage layer (point, line, etc.)
   * Specify the layer coordinate reference system
   * Create the fields that will be in the layer’s **Attribute Table** by giving them a
     name and indicating their type (text data, integer, etc.) under **New Field**. When
     you click on **Add to Fields List**, the new field will show up in the Fields List box.
3. Click **Ok**. Your new layer will appear in the **Layers** panel. If it is
   within another Group you do not want it in, right click on it and select
   **Move Out of Group**.  You can also drag and drop your layer into the
   location you want it.


## Creating a Custom Clipping Boundary Polygon

You can create your own custom boundary polygon layer to extract features
from. Follow the instructions above on [Creating New Vector
Layers from
Scratch](#creating-new-vector-layers-from-scratch) to draw a
polygon layer from scratch. Then, follow the instructions on [Selecting for
Greenland-Specific Vector Data](#selecting-for-greenland-specific-vector-data) to
extract features from vector layers using the custom polygon boundary layer
instead of the "Greenland coastlines 2017" layer.


## Importing GPS and other GNSS Data

QGIS supports importing Global Positioning System (GPS) and other Global
Navigation Satellite System (GNSS) data from GPS Exchange Format (GPX)
datasets. In the **Menu Bar**, go to **Layer -> Add Layer -> Add GPX Layer**.

QGIS can also interface with a GPS device to download data directly and provide
live tracking.

Please see the QGIS documentation on [Working with GPS
Data](https://docs.qgis.org/3.28/en/docs/user_manual/working_with_gps/index.html)
for more information.
