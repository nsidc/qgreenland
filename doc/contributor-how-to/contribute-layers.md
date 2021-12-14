# How to contribute new layers

It's recommended to use the CLI to create a dataset and/or layer template to
help you along. In the below commands, replace filenames, paths, and ids with
real ones. NOTE: When generating templates, but _not_ when fetching, you can
use `./scripts/experimental/local_cli.sh config-template <dataset|layer>` in
place of the `cli.sh` commands.

## Add a dataset

If the layer does not use an existing dataset, start with a new dataset.

```
./scripts/cli.sh config-template dataset > \
  qgreenland/config/datasets/new_dataset.py
```

## Fetch the data

Test the dataset by fetching the data:

```
./scripts/cli.sh fetch new_dataset_id
```
NOTE: If your fetch command results in an error, there may be issues with 
the entry of your dataset. Go back to your dataset.py file and 
make sure that all fields are filled in (abstract, title, etc.) to avoid linting errors.

## Create new layer

To create a layer, create new layer directories as needed, and then define your
new layer in a Python file with a descriptive name within the appropriate layer
group.

```
./scripts/cli.sh config-template layer > \
  qgreenland/config/layers/Group/Subgroup/new_layer.py
```

## Dataset requirements

In order for a new dataset to be added to QGreenland, we strongly encourage
public archival with OGC-compliant metadata. If data is not publicly archived
or stored in a non-standard format, maintenance of that layer takes an order of
magnitude more effort and therefore we are unable to promise permanent
inclusion of such data. File formats that are particularly challenging include:
raw binary grids, Excel files, Word documents. We prefer GeoTIFFs or NetCDFs
for raster data, and GeoPackages or shapefiles for vector data. 

A correct QGreenland data pipeline will output data that:

* Is in EPSG:3413. This is to reduce load on QGIS caused by on-the-fly
  reprojection. Some exceptions may exist in the current code as a workaround,
  but they are bugs.

* Is subset to one of the defined layer boundaries in `config/project.py`.
  Existing layer tasks can do this for vector or raster data.

* For raster data:
  * In GeoTIFF (`.tif`) format.
  * Includes overviews, for raster data. This improves QGIS performance.
  * Is losslessly compressed using the DEFLATE algorithm.

* For vector data:
  * In GeoPackage (`.gpkg`) format.
  * Uses the `label` attribute name for pre-calculated labels when using
    generic styles with labels, for example `labeled_point.qml`
