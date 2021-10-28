# Architecture

This project uses a `luigi` pipeline to generate the QGreenland package. Luigi
is a workflow management system developed by Spotify:
[https://github.com/spotify/luigi](https://github.com/spotify/luigi).

This project is currently undergoing rapid development, so expect change in any
release except releases labeled as "stable". Stable releases can be found at
[https://qgreenland.org/explore](https://qgreenland.org/explore)!


## Configuration

The QGreenland configuration represents the work that needs to be done to
convert source `datasets` in to final outputs ready for use by QGreenland. The
configuration can be found at:

```
qgreenland/config
```

Within this directory, there is a subdirectory for `datasets`, `layers`, and
`helpers`. Additionally, the `project.py` file is required in the config
directory.  You can optionally add any number of other files, e.g.
`constants.py`, to the configuration directory.

Configuration models can be found at:

```
qgreenland/models/config
```


### Project config

[project.py](/qgreenland/config/project.py) defines the project `crs` (EPSG) and
any `boundaries` that will be used to clip data for this project.


### Datasets config

Dataset configurations define a unique `id`, `metadata`, and a list of
`assets`.  

[Example](../qgreenland/config/datasets/background.py)


#### Assets

An asset represents a file or files in a dataset that will be used to create a
single layer. A layer currently cannot use more than one asset as its input.

There are various types of assets. Some useful ones are:

* `ConfigDatasetHttpAsset`: Downloads from a list of HTTP `urls`.
* `ConfigDatasetCmrAsset`: Queries NASA CMR for a single `granule_ur` in a
  given `collection_concept_id` and downloads it.
* `ConfigDatasetCommandAsset`: Runs an arbitrary command `args` to download or
  create data files.
* `ConfigDatasetManualAsset`: Accesses data that has been manually downloaded
  by a human in to the private archive. This is required for datasets which
  can not be fetched programmatically, for example: because they're behind a
  GUI authentication screen; because an asynchronous ordering system must be
  used to access the data; or because the data was provided directly by a
  scientist over e-mail and is not hosted anywhere. We prefer to avoid or
  eventually fully eliminate the use of data in this category.

You can find the full set of available asset types
[here](../qgreenland/models/config/assets.py).


### Layers and layer groups config

Layers in `qgreenland/config/layers` are organized into a directory structure
which mirrors the QGIS Layers Panel tree structure. Each directory may
optionally contain a settings file which is documented below in the [Layer
group settings](#layer-group-settings) section.

Layers can be represented in python files with any name. `ConfigLayer` objects
will be found in those python files when written either as plain named
variables, e.g. `foo = ConfigLayer(...)` or when present in a tuple or list,
e.g. `layers = [ConfigLayer(...) for thing in things]`.

The layer's `title` will determine how the layer is displayed in the QGIS
Layers Panel and the `description` determines the hovertext for that same layer
in the QGIS Layers Panel.


#### Layer steps

Layers are created in a series of `steps`. The final result of the `steps` must
be a GeoTIFF (`.tif` file) for raster layers, and a GeoPackage (`.gpkg`) for
vector layers.

Each step is a [command](../qgreenland/models/config/step.py) (e.g. `gdalwarp` or
`ogr2ogr`) run against the output of the previous step.  The first step acts on
the chosen `input.asset`. 

Within a step configuration, "runtime variables" are used to populate values
that are not known at configuration-time, for example the WIP directories that
will be used to store the inputs and outputs of the step. Runtime variables are
designated by braces `{` `}` surrounding the variable name. Only the following
runtime variables are legal:

* `{input_dir}`: The output directory of the previous step or, for the first
  step, the layer's fetched `input.asset` location.
* `{output_dir}`: The output directory of this step.
* `{assets_dir}`: In this repository, `qgreenland/assets`.


#### Layer group settings

Each layer group can optionally have a `__settings__.py` file inside its
directory which determines settings for only that group. If the file is
omitted, defaults are used (see [here](../qgreenland/models/config/layer_group.py)
for default values).

This file is most commonly used for specifying the order in which the layer
group's contents will be displayed in QGIS. If `order` is not specified,
contents are displayed alphabetically with groups first.

An [example](../qgreenland/config/layers/Reference/__settings__.py) settings file
shows that layers are represented with a leading `:` to differentiate layers
from groups in the same list.


### Helpers

Helpers are arbitrary python code to allow code-sharing between configuration
modules. The following categories of helpers exist in subdirectories:

* `layers`: Helpers and variables for generating layer configuration objects.
* `steps`: Helpers which return a step or steps configuration objects.
* `ancillary`: JSON data to support helpers.


### Lockfile

Use `inv config.export > qgreenland/config/cfg-lock.json` to refresh the
configuration lockfile. This allows us to compare the _results_ of
configuration changes against the previous state.


# The project pipeline

* Fetch input assets
* Run layer pipelines, writing outputs to final layer hosting locations.
* For layers for which `in_package` is `True`, use hardlinks to link final
  layer ouputs to a QGreenland package compile location.
* Create QGreenland package QGIS project file and other ancillary package
  files.
* Zip the QGreenland package.


# Running the project

## Starting the services

This project uses Docker and `docker-compose` to run each of its components.
https://docs.docker.com/get-started/

The docker-compose stack runs Luigi (with visualizer at port 8082) as a service
for running tasks, as well as NGINX (port 80, 443) for hosting outputs.

In order to download data behind Earthdata Login, you must `export` the
following environment variables on the docker host before starting the stack:

* `EARTHDATA_USERNAME`
* `EARTHDATA_PASSWORD`

Developers at NSIDC may use the values stored in Vault at the following path:
`nsidc/apps/qgreenland`. Those outside of NSIDC must use their personal
Earthdata Login credentials. New users to Earthdata can register here:
https://urs.earthdata.nasa.gov/users/new


### Starting the stack locally

Ensure environment variables enumerated above are populated before starting the
stack.

Create a [docker-compose
override](https://docs.docker.com/compose/extends/#understanding-multiple-compose-files)
file for `./logs` and `./appdata`.

```
ln -s docker-compose.local.yml docker-compose.override.yml
```

*WARNING*: Docker Desktop for OSX has some "gotchas". Running with "Use gRPC
FUSE for file sharing" _enabled_ is recommended. You may see indefinite hangs
otherwise. Please reference the Docker documentation for more info:

https://docs.docker.com/desktop/mac/

Start the stack with docker-compose:

```
docker-compose up -d
```


## Running pipelines with the QGreenland CLI

The primary entrypoint for the CLI is `./scripts/cli.sh`. This runs the CLI
program inside the `luigi` container, allowing us to kick off pipelines or
cleanup data from standard locations without risking destructive actions on the
user's computer.

To run the full pipeline:

```
./scripts/cli.sh run
```

To run in parallel:

```
./scripts/cli.sh run --workers=4
```

To run only the layers you care about (plus the background, useful for
testing, but the final output will not be zipped):

```
./scripts/cli.sh run \
  --include="background" \
  --include="*my_layer_mask*"
```

Collaborators outside NSIDC may want to run QGreenland pipeline without "manual
access" layers that require difficult or impossible additional steps to prepare
input data. See [Assets](#assets) documentation above to learn more about
"manual access" assets.

```
./scripts/cli.sh run \
  --exclude-manual-assets
```

Inclusion and exclusion flags can be combined arbitrarily. When `--include` and
`--exclude` are used together, the final result is the set of layers which are
included _or_ not excluded. This is different from the set of layers which are
included _and_ not excluded.

To cleanup outputs (compiled package and releases):

```
./scripts/cli.sh cleanup -C True -R True
```

See the [Luigi
documentation](https://luigi.readthedocs.io/en/stable/running_luigi.html) for
more information on running Luigi if you want to do anything not documented
here.


### Debugging a Luigi pipeline

Simply put `breakpoint()` anywhere in the pipeline code, then run the pipeline
with 1 worker (the default) and whichever layer(s) you want to debug.


# Contributing

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

Create new layer groups as needed, and then define your new layer in a Python
file with a descriptive name within the appropriate layer group.

It's recommended to use the CLI to create a dataset or layer template to help
you along. In the below commands, replace filenames and paths with real ones.

```
./scripts/cli.sh config-template dataset > \
  qgreenland/config/datasets/new_dataset.py
./scripts/cli.sh config-template layer > \
  qgreenland/config/layers/Group/Subgroup/new_layer.py
```

NOTE: You can use `./scripts/experimental/local_cli.sh` instead, which does not
require the QGreenland docker stack to be running.


### Layer requirements

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


# Releasing

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
