# Create a layout for print or publication

QGIS is a powerful data viewing and analysis platform, but it is also capable of
creating publication-quality maps for print or publiction. This tutorial covers
the basics of creating a new print layout in QGIS, adding a map and map elements
to that layout, and exporting the resulting layout as an image.

See the [QGIS
manual](https://docs.qgis.org/3.16/en/docs/training_manual/map_composer/map_composer.html)
for complete documentation on print layouts in QGIS.


##  Creating a new print layout

Once one has created a map in the **QGIS map display** that one would like to print
or publish, one needs to switch to the **QGIS print layout**. Select **"Print Layout"**
from the "Project" menu.

```{note}
The **Project Toolbar** ![project_toolbar](/_images/project_toolbar.jpg) also
contains a button (![print_layout_button](/_images/print_layout_button.jpg))
that creates a new **Print Layout**.
```

First, name the new print layout after the figure you plan to create and click
**"OK"**.

![print_layout_name](/_images/print_layout_name.jpg)

When the print layout window opens, it will be initially blank.

![blank_print_layout](/_images/blank_print_layout.jpg)

## Changing the print layout's properties

To change the size and orientation of your print layout, right click in the map
area and choose **"Page Properties"**. This will add page size options to the **Item
Properties** panel on the right side of the screen.

![print_page_properties](/_images/print_page_properties.jpg)

## Adding a map and other elements

The print layout will allow you to add features to your map such as a title,
legend, north arrow, scale bar, pictures, etc by interacting with the buttons in
the **Toolbar** on the left of the screen.

To add a map to your layout, click on the **Add Map** button
![print_add_map](/_images/print_add_map.jpg). Click and drag to create a box
where the map will appear on the print layout display.

![map_layout_with_map](/_images/map_layout_with_map.jpg)

To zoom into the region shown in the map or change the extent, click on the
**Move Item Content** button
![move_item_content](/_images/move_item_content.jpg), which will make it
possible to manipulate the map area within the box.

Now explore some of the other buttons included in the map layout Toolbar. Add a
north arrow and scale bar. Finally, once one is happy with the layout, try
exporting the layout as an image by opening the **"Layout"** menu and selecting
**"Export as Image"**.

## Summary

In completing this tutorial, the user has created a new print layout, added a
map and other elements to the layout, and exported the layout as an image. This
image can now be utilized in publications or printed to physical media (e.g., a
poster).
