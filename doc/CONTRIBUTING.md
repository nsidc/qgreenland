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
  --include="*my_layerid_mask*"
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

To cleanup outputs while developing a new layer (deletes WIP and released
layers matching mask, WIP and released packages; see `--help` for more):

```
./scripts/cli.sh cleanup --dev '*my_layerid_mask*'
```

See the [Luigi
documentation](https://luigi.readthedocs.io/en/stable/running_luigi.html) for
more information on running Luigi if you want to do anything not documented
here.


### Debugging a Luigi pipeline

Simply put `breakpoint()` anywhere in the pipeline code, then run the pipeline
with 1 worker (the default) and whichever layer(s) you want to debug.


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
