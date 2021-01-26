# Categorical Data

Categorical data can be raster or vector, but styling considerations are
similar either way.

Use the "Paired" color palette from cpt-city with 10 colors for Categorical
data. You can use this colormap without leaving the QGIS user interface.

TODO: Pick a better color ramp or palette.


# Raster Data

## Colormaps

TODO: Find better typenames


### Scalar

Colormaps should be limited to N "classes" to reduce vertical space taken in
the Layers Panel by the legend.

TODO: How many elements?


# Vector Data

## Protected Areas

### Colors

Any color from this pallette:

    http://soliton.vm.bytemark.co.uk/pub/cpt-city/cb/seq/tn/YlOrRd_09.png.index.html

TODO: Standards for colors. What do they mean?


### Polygon

Example: "Arctic Protected Areas (CAFF 2017)" for an example.

Protected area polygons will use a "Line pattern fill" with rotation of 45° to
produce a "hashed" pattern. Lines will be solid, thickness will be 0.3mm,
spacing will be 2mm. Border and lines will be the same color.

Labels displayed over the hashed polygon will have a buffer of at least 2mm with 100% opacity.
