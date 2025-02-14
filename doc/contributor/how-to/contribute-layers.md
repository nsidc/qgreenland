# How to contribute new layers

```{note}
We cannot promise that your layer will be added, so please [open an
issue](https://github.com/nsidc/qgreenland/issues/new/choose) and start a
discussion before developing a processing pipeline for a new layer. 
```

It is recommended to use the CLI to create a dataset and/or layer template to
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
After running the command above, a new_dataset.py file will 
be populated with dataset information that is needed to create 
a layer. Make sure that the abstract and title are filled out.

## Fetch the data
Once you are finished filling in the dataset information, you can try 
testing the dataset by fetching the data:

```
./scripts/cli.sh fetch new_dataset_id
```
```{note}
If your fetch command results in an error, there may be issues with 
the entry of your dataset. Go back to your dataset.py file and 
make sure that all fields are filled in (abstract, title, etc.) to avoid linting errors.
```

## Create new layer

The next step is to create the new data layer. To do this, create new layer 
directories as needed, and then define your new layer in a Python file with 
a descriptive name within the appropriate layer group.

You can do this by running this command:
```
./scripts/cli.sh config-template layer > \
  qgreenland/config/layers/Group/Subgroup/new_layer.py
```

The above command generates a new_layer.py file. Once you see this file,
follow the documentation within the file to fill out your layer configuration.

```{note}
If the group directory where you have created your layer file has a __settings__.py file,
you must add your new group to the 'order' list of this file. Make sure it is spelled 
exactly the same as in your file structure.
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


## Layer quality checklist

### All layers

- Abstract populated
- Citation populated
- Layer descriptions populated
- Layer description excludes data provider
- Layers'/groups' title follows date standard: If a layer is date-specific, the date
  should be the last part of the title except the resolution, if present. Not in
  parentheses or otherwise distinguished from the rest of the title. Format is "Month
  DD YYYY" (all fields optional), e.g.:
    - `Common Murre Colonies 2010`
    - `Sea Ice Age September 17-24 2010`
- Layers'/groups' title follows capitalization standard: Capitalize first letter of the
  Title. Other than this, only capitalize proper nouns and acronyms. E.g.:
    - `Thickbilled Murre 1km breeding zone`
- Layers'/groups' title excludes data provider: Layer should not include provider e.g.
  "NSIDC". Put this in the dataset citation instead! _EXCEPTION:_ In some cases, we have
  the same type of data from various providers, e.g.:
    - `Discipline/Measurement/Provider A/Layer`
    - `Discipline/Measurement/Provider B/Layer`
- No fields are populated with "TBD" or "TODO"
- All layers have style
- Any known issues with data quality are listed in "Description": This should not
  include spatial mismatch issues, this is covered by our [Disclaimer](/disclaimer.md).
- Datastore's data is the latest: Some layers get updated perioidically e.g.,
  earthquakes.
- Layers not in unneccessary group
- Stakeholders approve citation
- Stakeholders approve description


### Raster layers

- When reprojecting (e.g. via `gdalwarp` or adding overviews (e.g. via `gdaladdo`),
  ensure the interpolation algorithm follows standard:
    - Bilinear for continuous values (i.e. real), e.g. temperatures, height. By default,
      everything is bilinear.
    - Nearest neighbor for discrete (i.e. integer) values, e.g. population.
- Grid resolution in layer title or group (incl. units), e.g. `My layer (1km)`
- When a layer is reprojected (e.g., via `gdalwarp`), ensure that the
  target resolution is explicitly specified. Sometimes when the output resolution is not
  defined, GDAL will choose a resolution that is not appropriate for the data, and this
  can lead to artifacts.


### Vector layers

- Polygon labels inside polygons
- All attributes have reasonable types (e.g,. a `population` attribute should be an integer type, not string)
