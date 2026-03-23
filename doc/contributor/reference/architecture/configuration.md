# Configuration


The QGreenland configuration represents the processing that needs to be done to
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


## Project config


{github}`project.py <qgreenland/config/project.py>` defines the project `crs` (EPSG) and
any `boundaries` that will be used to clip data for this project.


(configuration-datasets-config)=
## Datasets config

Dataset configurations define a unique `id`, `metadata`, and a list of
`assets`.

{github}`Example <qgreenland/config/datasets/background.py>`


### Assets

An asset represents a file or files in a dataset that will be used to create a
single layer.

There are various types of assets. Some useful ones are:

* {class}`~qgreenland.models.config.asset.HttpAsset`: Downloads from a list of HTTP `urls`.
* {class}`~qgreenland.models.config.asset.CmrAsset`: Queries NASA CMR for a single `granule_ur` in a
  given `collection_concept_id` and downloads it.
* {class}`~qgreenland.models.config.asset.CommandAsset`: Runs an arbitrary command `args` to download or
  create data files.
* {class}`~qgreenland.models.config.asset.ManualAsset`: Accesses data that has been manually downloaded
  by a human in to the private archive. This is required for datasets which
  can not be fetched programmatically, for example: because they're behind a
  GUI authentication screen; because an asynchronous ordering system must be
  used to access the data; or because the data was provided directly by a
  scientist over e-mail and is not hosted anywhere. We prefer to avoid or
  eventually fully eliminate the use of data in this category.

You can find the full set of available asset types
{github}`here</qgreenland/models/config/asset.py>`.

(configuration-layers-and-layer-groups-config)=
## Layers and layer groups config

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


### Layer inputs

A layer can be created from multiple `inputs`, which is given by a list of
`LayerInputs`, each of which references a specific dataset and an asset within
that dataset. For example, the `nunagis_municipalities` layer has two
inputs which are combined together to create the output layer in QGIS:


```
inputs=[
    # This input provides a multipolygon of municipalities and population numbers for 2019
    LayerInput(
        dataset=political_boundaries.nunagis_pop2019_municipalities,
        asset=political_boundaries.nunagis_pop2019_municipalities.assets["only"],
    ),
    # This input provides updated population statistics for 2025 (Jan 1, 2026).
    LayerInput(
        dataset=statbank.statbank,
        asset=statbank.statbank.assets["municipalities_2025_population"],
    ),
],
```

When multiple inputs are used, the data from each are combined into a single
`{input_dir}` via symlinks for the layer's first step. The layer's first step
must act on all inputs - layer inputs are not propagated to subsequent steps!
See {ref}`configuration-layer-steps` for more.


```{admonition} WARNING
Layer inputs are expected to have unique filenames. The symlinking process does
not handle conflicts!

```

#### Online-only layers

Some layers are pointers to web map services. These layers are distinguished
from others by having a single `LayerInput` specifying an `OnlineAsset`. When an
`OnlineAsset` is used in a layer's inputs, it must be the only input. No data
processing steps are applied to these layers since they just display data from
an online source.

#### Virtual vector layers

A virtual vector layer is a layer that references another vector layer in the
project. These layers are identified by the presence of a single
`VectorLayerReferenceInput` (instead of a `LayerInput`). The
`VectorLayerReferenceInput` is handy when one wants to create a layer simply
displays the data from another layer in a unique way, without duplicating the
data.

The primary use-case for virtual vector layers are timeseries layers that have a
temporal controller configuration. The QGIS temporal controller assumes there is
one geometry per timestamp. For some layers, this is problematic because the
geometry is static (e.g., Greenland's municipalities polygons), but the
population label we apply to it changes over time. The
`VectorLayerReferenceInput` allows one to reference another layer and use SQL to
define a view of the data that prevents duplicating data on disk.

Example configuration:

```
VectorLayerReferenceInput(
    layer_id="nunagis_municipalities",
    sql=(
        """SELECT
            municipalities.geom,
            municipalities.municipality,
            pop.start_date,
            pop.end_date,
            pop.\"Population January 1st\" as population
            FROM municipalities
            RIGHT JOIN pop ON pop.municipality
            = municipalities.municipality"""
    ),
)
```

In this example, the layer with ID `nunagis_municipalities` is being
referenced. its data file contains two tables, "municipalities" and "pop". The
municipalities table contains the geometries for Greenland's municipalities and
it is joined to the "pop" table containing 50 years of population numbers for
each municipality.

Virutal vector layers are represented on disk as `.vrt` files in the final output:

```
<OGRVRTDataSource>
    <OGRVRTLayer name="municipalities_and_population">
        <SrcDataSource relativeToVRT="1">../../../Reference/Borders/Greenland municipalities/nunagis_municipalities.gpkg</SrcDataSource>
        <SrcSQL>SELECT municipalities.geom, municipalities.municipality, pop.start_date, pop.end_date, pop."Population January 1st" as population FROM municipalities RIGHT JOIN pop ON pop.municipality = municipalities.municipality</SrcSQL>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

Note that virtual vector layers have no processing applied from them and inherit
metadata from the referenced data layer.


(configuration-layer-steps)=
### Layer steps

Layers are created in a series of `steps`. The final result of the `steps` must
be a GeoTIFF (`.tif` file) for raster layers, and a GeoPackage (`.gpkg`) for
vector layers.

Each step is a {github}`command </qgreenland/models/config/step.py>` (e.g. `gdalwarp` or
`ogr2ogr`) run against the output of the previous step.  The first step acts on
the chosen `inputs`.

Within a step configuration, "runtime variables" are used to populate values
that are not known at configuration-time, for example the WIP directories that
will be used to store the inputs and outputs of the step. Runtime variables are
designated by braces `{` `}` surrounding the variable name. Only the following
runtime variables are legal:

* `{input_dir}`: The output directory of the previous step or, for the first
  step, the layer's fetched `inputs` location.
* `{output_dir}`: The output directory of this step.
* `{assets_dir}`: In this repository, `qgreenland/assets`.


### Layer group settings

Each layer group can optionally have a `__settings__.py` file inside its
directory which determines settings for only that group. If the file is
omitted, defaults are used (see
{github}`here </qgreenland/models/config/layer_group.py>` for default values).

This file is most commonly used for specifying the order in which the layer
group's contents will be displayed in QGIS. If `order` is not specified,
contents are displayed alphabetically with groups first.

An {github}`example </qgreenland/config/layers/Reference/__settings__.py>` settings file
shows that layers are represented with a leading `:` to differentiate layers
from groups in the same list.


## Configuration helpers

Helpers are arbitrary python code to allow code-sharing between configuration
modules. The following categories of helpers exist in subdirectories:

* `layers`: Helpers and variables for generating layer configuration objects.
* `steps`: Helpers which return a step or steps configuration objects.
* `ancillary`: JSON data to support helpers.


## Configuration lockfile

Use `inv config.export > qgreenland/config/cfg-lock.json` to refresh the
configuration lockfile. This allows us to compare the _results_ of
configuration changes against the previous state.
