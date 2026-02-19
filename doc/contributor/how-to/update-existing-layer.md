# How to update existing layers

## Identify the layer and dataset configuration

Start by identifying the layer you want to update in QGreenland. For example,
this might be `Human activity/Research sites/Seismograph stations`. To find the
layer configuration in the `qgreenland` code, look in the associated
subdirectory of `qgreenland/config/layers/`. For the Seismograph stations layer,
this would be `qgreenland/config/layers/Human activity/Research sites`.

```{note}
Layer configuration is setup to mirror the layout of the table of contents in
QGIS. To change the order of layers or layer groups, see the `__settings__.py`
in the subdirectory in which you want to make a change.
```

From the layer configuration, it should be easy to identify the dataset
configuration. Look for an import of a dataset at the top of the layer
configuration file. For example, the import for `Seismograph stations` may look
like:

```
from qgreenland.config.datasets.seismograph_stations import (
    seismograph_stations as dataset,
)
```

In this case, the dataset config can be found in
`qgreenland/config/datasets/seismograph_stations.py`


## Update dataset configuration

When a dataset is updated, it is usually necessary to update the dataset
configuration to reflect the new version. Make sure to check the title,
citation, and abstract for necessary updates.

If the location(s) of the source data has changed (e.g., the URL is different),
update the `assets` list.

## Try fetching the updated data

Once the datasaet configuration has been updated, you should try testing out the
configuration by fetching the data.

First, cleanup the existing dataset. This can be accomplished with the `cleanup`
subcommand of the CLI. The `-f` flag lets you specify what you want to cleanup
by passing it a dataset ID or a pattern that matches it. Below, we cleanup
any fetched data with `seismograph_stations` in the name.

```
./scripts/cli.sh cleanup -f "*seismograph_stations*"
```

Next, try fetching the data with the `fetch` subcommand, providing a similar
pattern:

```
./scripts/cli.sh fetch --workers 1 "*seismograph_stations*"
```

Assuming the fetch is successful, you may want to manually check the fetched
data. It can be found in the `data/working-storage/fetch-datasets/` directory:

```
$ ls data/working-storage/fetch-datasets/seismograph_stations.only/
stations.kmz
$ ogrinfo -summary data/working-storage/fetch-datasets/seismograph_stations.only/stations.kmz
INFO: Open of `data/working-storage/fetch-datasets/seismograph_stations.only/stations.kmz'
      using driver `LIBKML' successful.
1: International Registry of Seismograph Stations
```

## Update layer configuration

Once you have successfully fetched the updated data, it is time to update the
layer configuration.

Check the title and description of the layer and update as needed.

Consider any relevant changes to the style (see TODO: link to style guide) for more info.

Finally, check the `steps` configuration and determine if any tweaks need to be
made given the updated data. For example, if the updated dataset uses a new
filename or file format, these steps may need to change.


## Run QGreenland with the changes

After the dataset and layer configuration are updated, you can test the
QGreenland processing pipline with the `run` subcommand. 


### Pre-run cleanup
Before a new `run`, cleanup intermediate/work-in-progress (WIP) data. Without
this step, the code might report that the processing is already complete and
nothing needs to be done.

Below, the first command cleans up release layers, WIP packages, and release
packages. The second command cleans up WIP layers matching the given pattern, in
this case `*seismograph*`.

```
./scripts/cli.sh cleanup -RL -WP -RP
./scripts/cli.sh cleanup -wl "*seismograph*"
```

### Building the package with `run`

The `--include` flag can be used to limit the number of layers processed to
speedup an otherwise long build. The `-Z` flag prevents the final zip step that
zips the package up for distribution, also saving time for testing.

```
./scripts/cli.sh run -Z --include="*coastline*" --include "*earthquake*" --include "*seismograph*"
```

Note that in the example above, we include the coastline and earthquake layers
in addition to the newly updated `seismograph_stations` for reference purposes.

## Check the output

Assuming the run was successful, check the output to ensure that the updates
have been correctly applied. The newly built package is in
`data/working-storage/wip-package/QGreenland`. Open the
`data/working-storage/wip-package/QGreenland/qgreenland.qgz` in QGIS and
manually inspect the data.

## Lock the config

After confirming that the new layer updates are successful, run the following
command to update the config lock file:

```
inv config.export > qgreenland/config/cfg-lock.json
```

## Update the CHANGELOG

Update the `CHANGELOG.md`, indicating what layers were updated. If needed, bump
the version for a new release.

## Open a Pull Request

Finally, open a Pull Request (PR) on GitHub with the changes in a new branch that is
named in a descriptive way.
