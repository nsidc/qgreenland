This project is currently undergoing rapid development, so expect change in any
release except releases labeled as "stable". Stable releases can be found at
[https://qgreenland.org/explore](https://qgreenland.org/explore)!


# The processing pipeline

* Fetch input assets
* Run layer pipelines, writing outputs to final layer hosting locations.
* For layers for which `in_package` is `True`, use hardlinks to link final
  layer ouputs to a QGreenland package compile location.
* Create QGreenland package QGIS project file and other ancillary package
  files.
* Zip the QGreenland package.



# Running the project

See [How to run QGreenland](doc/how-to/RUN_QGREENLAND.md).


# Contributing to the project

One of the primary goals of this project is to allow for scientists comfortable
with standard GIS command-line tools to contribute new layers with as little
friction as possible.

Contributing new datasets and layers requires writing simple Python objects
containing the relevant data (metadata, download location, transformation
steps) needed to include the layer in QGreenland.

Currently, layer styles can be contributed without any programming knowledge by
designing the style in QGIS, saving it as a `.qml`, and committing it to the
`qgreenland/ancillary/styles` directory.

You can contribute to this project even if you don't have write access by
forking, making your change, making all CI checks pass, then opening a Pull
Request. Learn more:

https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork


## Contributing styles

You can contribute style changes without editing any Python code using the
following process:

* Download (or build) and open the most recent version of the project in QGIS.
* In the 'Layers' menu, double click on the layer you wish to edit.
* Open the 'symbology' tab.
* Make your desired style changes.
* In the lower-left corner, click the 'Style' dropdown.
* In this menu, select 'Save Style...'

![Save style](images/save_style.png)

* At this point, if you're uncomfortable with Git and GitHub, you can email us
  your style file at qgreenland.info@gmail.com. Otherwise, continue on...
* Save the style to `qgreenland/assets/styles/<name>.qml` directory of this
  repository or your fork. Keep in mind that styles can be shared between
  layers, so give the style a generic name instead of a layer-specific name
  where possible.
* Edit the relevant layer configuration file in `qgreenland/config/layers` and
  find the layer(s) you wish to apply this style to. Populate the `style`
  attribute for each layer with the name of the `.qml` file you saved in the
  previous step, excluding the file extension. For example, if you saved
  `foo.qml`, then populate `style='foo'`.

![Style in YAML](images/style_in_yaml.png)


## Contributing new layers

It's recommended to use the CLI to create a dataset and/or layer template to
help you along. In the below commands, replace filenames, paths, and ids with
real ones. NOTE: When generating templates, but _not_ when fetching, you can
use `./scripts/experimental/local_cli.sh config-template <dataset|layer>` in
place of the `cli.sh` commands.

If the layer does not use an existing dataset, start with a new dataset.

```
./scripts/cli.sh config-template dataset > \
  qgreenland/config/datasets/new_dataset.py
```

Test the dataset by fetching the data:

```
./scripts/cli.sh fetch new_dataset_id
```

To create a layer, create new layer directories as needed, and then define your
new layer in a Python file with a descriptive name within the appropriate layer
group.

```
./scripts/cli.sh config-template layer > \
  qgreenland/config/layers/Group/Subgroup/new_layer.py
```


### Dataset requirements

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


# Releasing a new version of the code

Use `bumpversion` to bump the specified part of the version:

```
$ bumpversion --part={major|minor|patch}
```

Versions should be in one of the following forms:

* `vX.Y.ZalphaN`: An alpha pre-release, e.g. `v1.2.3beta2`
* `vX.Y.ZbetaN`: A beta pre-release, e.g. `v1.2.3alpha2`
* `vX.Y.ZrcN`: A release candidate, e.g. `v1.2.3rc3`.
* `vX.Y.Z`: A final release, e.g. `v1.2.3`.

NOTE: When using `bumpversion build`, ensure you've already used `bumpversion
prerelease`. Running `bumpversion build` from a final release version number
can result in an incorrect patch number, e.g. `v1.2.304`.

Publishing a tag to GitHub will trigger an automated build and publish of the
QGreenland package to various mirrors.

Creating a "Release" in GitHub will trigger archival of our code in Zenodo and
issuance of a new DOI. Do _not_ create a "Release" in GitHub until a new
version of the package has been successfully built and pushed to mirrors.
