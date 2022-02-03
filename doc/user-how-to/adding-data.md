# Adding New Datasets to QGreenland

Once the QGreenland package is downloaded onto a user’s computer, it is fully customizable
by the user. One can add new data, delete layers within QGreenland, or make changes.
Saving the project will update the qgreenland.qgs project file. If you don’t want to overwrite
the original project version, simply save your updated project using a new filename via ‘Save
As...’ You can create as many different projects as you like, adding or removing data from the
downloaded QGreenland package or adding data from elsewhere on your computer.

## Uploading New Layers to QGreenland

## Selecting for Greenland-Specific Data

Because the geographic extent of some QGreenland data layers extends beyond the
geographic and political border of Greenland to include the surrounding water bodies
and land masses, it might sometimes be necessary to filter out certain data if one is only
interested in data within Greenland’s geographic boundary. You can do this using the
Greenland coastlines 2017 polygon layer.

To add new data layers to QGreenland:
1. In the **Menu Bar**, go to **Layer -> Add Layer**, and choose the layer type you
   want to add. Alternatively, you can either click on the desired add layer button
   in the toolbar, or click on the **Data Source Manager** button in the **Data Source Manager** toolbar.
2. Any option you choose will open the same **Data Source Manager** window. On
   the right side of the window, you can double check that the layer type you want
   to add is highlighted.
3. Navigate to the data file that you want to add as a layer, then click **Add**.

## Selecting for Greenland-Specific Data

Because the geographic extent of some QGreenland data layers extends beyond the
geographic and political border of Greenland to include the surrounding water bodies
and land masses, it might sometimes be necessary to filter out certain data if one is only
interested in data within Greenland’s geographic boundary. You can do this using the
Greenland coastlines 2017 polygon layer.

To filter out data outside of Greenland:
1. Make sure that the group you want the filtered/extracted data to be added to is
   selected/highlighted in the **Layers** panel.
2. Open the Processing Toolbox and go to **Vector selection -> Extract by location**.
3. Fill in the following parameters:
   -Extract features from = the data layer you want to filter, for example, Ice cores
   -Where the features (geometric predicate) = are within (you can also check intersect and
   others to capture data that might be located along the Greenland coastline)
   -By comparing to the features from = Greenland coastlines 2017
   -Extracted (location) = You can either save the file output from this as a temporary layer
   or as a permanent layer somewhere on your computer or within your QGreenland data
   package. Note: If you try to save the file as a GeoPackage layer (GPKG) and receive an
   error, try again and save it as a Shapefile (SHP) instead.
4. Click **Run** and close the window.

The filtered data will show up in the **Layers** panel within the group you had selected and likely
named **Extracted (location)**. You can rename the layer by right clicking on it and selecting
**Rename Layer**.

## Creating a Custom Clipping Boundary Polygon
You can create your own custom boundary polygon layer to extract features from. Follow the
instructions in section, **Creating New Shapefiles and GeoPackage Layers from Scratch**
to draw a polygon layer from scratch. Then, follow the instructions in section 6.2 Selecting
for Greenland-Specific Data to extract features from your custom polygon boundary layer;
however, instead of comparing features from the Greenland coastlines 2017 layer, you will
instead select the new custom boundary layer.

## Editing Vector Data Layers
How do you add or delete points, line segments, or polygons to/in an existing vector layer in
your QGreenland project?

To edit a vector layer:
1. Select the layer you want to edit in the **Layers** panel (click on it so that it is
   highlighted).
2. Toggle into editing mode by either right clicking on the vector layer you are
   editing in the **Layers** panel and selecting **Toggle Editing** or by clicking on the
   **Toggle Editing** button in the **Digitizing** toolbar.
3. With **Editing** on, you will have access to new editing buttons in the **Digitizing**
   toolbar:
   **Add new points to a point vector layer**
   **Add new lines to a line vector layer**
   **Add new polygons to a polygon vector layer**
4. Whenever you create any new vector feature, you will be prompted to enter
   attribute information for the new feature for its record in the layer’s **Attribute
   Table**.
5. If you just want to edit a record in a vector layer’s **Attribute Table**, you can open
   the **Attribute Table** and click on the **Toggle Editing** icon in the table toolbar. Be
   sure to save the layer edits after you’re done making edits.
6. When you’re finished, click on the **Toggle Editing** button again in the toolbar to
   disable editing.

## Creating New Shapefiles and GeoPackage Layers from Scratch

In your QGreenland project, you may want to create a new vector layer from scratch, such as
a point shapefile of potential study sites for for your research in Greenland. To draw a new vector
layer from scratch, you can either create a new shapefile or a new GeoPackage.

To create a new shapefile layer:
1. Go to **Layer’ -> Create Layer -> New Shapefile Layer** in the **Menu Bar** or click
on the New Shapefile **Layer** button in the **Data Source Manager** toolbar.
2. In the new window, specify the properties of your new layer, including giving it
a name, specifying its geometry (point, line, polygon) and coordinate reference
system (the coordinate reference system for all QGreenland data layers is
EPSG: 3413).
3. In the same window, create each field for your new layer’s **Attribute Table** under
**New Field**. You will need to specify whether the new field will contain text data
(string), whole number data (integer), decimal number data (real), or a date.
When you click **Add to Fields List**, the new field will show up in the **Field List**
below.
4. If you have a layer group highlighted in the Layers panel when you create
the new layer, the new layer will be automatically nested into the highlighted
group. You can move it out of the group by right clicking on the new layer and
selecting **Move Out of Group**.
5. Once the new layer has been created, add new features to it using the
processes described in section **Editing vector data layers**.

To create a new GeoPackage layer:
1. In the **Menu Bar**, go to **Layer -> Create Layer -> New GeoPackage Layer** or
click on the **New GeoPackage Layer** button in the **Data Source Manager**
toolbar.
2. A GeoPackage is a GIS file format that allows you to save multiple layers in one
file; thus, you will actually be creating a new GeoPackage database that your
new GeoPackage layer will live in. In the new window:
   -Name your new Database
   -Name the new GeoPackage layer you are creating - this is the **Table name**
   -Specify the geometry of the new GeoPackage layer (point, line, etc.)
   -Specify the layer coordinate reference system
   -Create the fields that will be in the layer’s **Attribute Table** by giving them a
      name and indicating their type (text data, integer, etc.) under **New Field**. When
      you click on **Add to Fields List**, the new field will show up in the Fields List box.
3. Click **Ok**. Your new layer will appear in the **Layers** panel. If it is within another
Group you do not want it in, right click on it and select **Move Out of Group**.
You can also drag and drop your layer into the location you want it.

In addition to shapefiles and GeoPackages, there are additional new layer types that can be
created also, such as **SpatialLite Layer** and **Virtual Layer**. Descriptions for all layer types can be
found in the **Reference** tab.

## Importing GPS and other GNSS Data Using the GPS Plugin

Importing GPS (Global Positioning System) or other GNSS (Global Navigation Satellite
System) data into QGIS requires an internal plugin. A plugin is just a new feature or function
that you can add to QGIS that does something one of the built-in tools doesn’t do. Many
plugins are ‘external’ meaning they are not developed and maintained by the QGIS
development team. Some plugins, however, are ‘core’ meaning they are maintained by the
QGIS team. The **GPS Plugin** is a core plugin and should already be installed in your version of
QGIS.

To turn on the **GPS Plugin**:
1. Go to **Plugins -> Manage and Install Plugins** in the **Menu Bar**.
2. Click on **Installed** in the left sidebar, then check the box next to **GPS Tools** in
the plugin list. If it is already checked, don’t change anything.
3. Click **Close**.

You can import GPS data either directly from a GPS device that is connected to your
computer, or from a file on your computer. Note that QGIS uses the GPX file format for GPS
data, although you can import GPS data that is not GPX (see #2c below).

To import GPS or GNSS data using the **GPS Plugin**:
1. Go to **Vector -> GPS Tools** in the **Menu Bar**.
2. In the window that pops up, click on the tab most appropriate for the data you
   want to import.
   a) If you are importing GPS data from a file on your computer, click on the **Load GPX file** 
      tab and navigate to the file on your computer. Indicate which feature
      types you want to load from the file (waypoints, routes or tracks), then click **Ok**.
      Each feature type you selected will be loaded in a separate layer.
   b) If you want to import data directly from a GPS device, click on the **Download from GPS** tab.
       i) Select the GPS device you are importing from, the port the device is
          connected to, and what feature types you want to download.
       ii) Give the data a layer name, which is what it will show up as in the
          **Layers Panel**.
       iii) The output file is where the downloaded data from your device will
         be stored on your computer. Click **Ok**. The data should appear as a
         new layer in the **Layers Panel**.
   c) To import GPS data that is not in the GPX file format, click on the 
      **Import other file** tab and fill in the relevant information.

