# Style guide

Styles live in `qgreenland/ancillary/styles`.

For more info on importing third-party colormaps in to QGIS, watch our YouTube
video: https://www.youtube.com/watch?v=rmYehinZa1U


## Standards

### Categorical Data

Categorical data can be raster or vector, but styling considerations are
similar either way.

Use the "Paired" color palette from cpt-city with 10 colors for Categorical
data. You can use this colormap without leaving the QGIS user interface.

```{tip}
TODO: Pick a better color ramp or palette.
```


### Raster Data

#### Colormaps

##### Scalar

Colormaps should be limited to 11 "classes" to reduce vertical space taken in
the Layers Panel by the legend.

Divergent colormaps should always contain an odd number of classes, and the
median class should represent the critical value in the data, e.g. 0 for
anomaly or "error" data.


### Vector Data

Vector data should primarily use colors from [Color
Brewer](http://colorbrewer2.org). These colors can be imported into QGIS via
cpt-city
[here](http://soliton.vm.bytemark.co.uk/pub/cpt-city/cb/seq/index.html).


#### Protected Areas

Use any color from Color Brewer's `YlOrRd09` color palette.


##### Polygon

Example: "Arctic Protected Areas (CAFF 2017)" for an example.

Protected area polygons will use a "Line pattern fill" with rotation of 45° to
produce a "hashed" pattern. Lines will be solid, thickness will be 0.3mm,
spacing will be 2mm. Border and lines will be the same color.

Labels displayed over the hashed polygon will have a buffer of at least 2mm
with 100% opacity.
