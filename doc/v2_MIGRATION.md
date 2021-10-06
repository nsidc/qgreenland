# About

## Create a new `git` branch

Avoid conflicts with other developers! Create a branch called
`migrate-{yourlayer}`.


## Select layers and datasets of interest

Examine the old QGreenland config:

    https://github.com/nsidc/qgreenland/tree/v1.0.2/qgreenland/config

Find the layer and dataset IDs you are interested in and note them for the next
steps.

The dataset ID is listed as `data_source` on the layer config in the format
`<dataset_id>.<source_id>`, e.g.:

    data_source: seismograph_stations.only


## Run dataset migration

Run the following command to create a basic migration of dataset(s). Validate
that it looks correct afterwards. Manual changes may or may not be required.

`./scripts/cli.sh config-migrate dataset {dataset_pattern} > config/datasets/{dataset}.py`

* Specifically examine the whitespace in large strings like `abstract` or
  `description` fields. Blank lines may need to be added to compensate for
incorrect YAML in the old format. Compare against the YAML as a guide.

## Run layer migration

### Prep directories

Ensure that the layer's group path is represented in the `layers/config`
directory structure. This can be found in the YAML config as, e.g.:

    group_path: 'Human activity/Research stations'

Please ensure that the capitalization of these directories is identical to the
text found in the old YAML config.

If layers are ordered in a special way, you may also need to create a
`__settings__.py` file in the root of new directories you've created. Follow
the example set in other directories. If you are adding a directory to an
existing directory with a `__settings__.py`, that file may need to be updated.


### Migrate

Run the following command to create a basic migration of layer(s). Validate
that it looks correct afterwards. Manual changes _WILL_ be required.

`./scripts/cli.sh config-migrate layer {layer_pattern} > config/datasets/{layer}.py`

* Look for `# TODO` markers in the output and fill those in. Don't forget to
  delete to TODOs!

* Specifically examine the whitespace in large strings like `abstract` or
  `description` fields. Blank lines may need to be added to compensate for
incorrect YAML in the old format. Compare against the YAML as a guide.
