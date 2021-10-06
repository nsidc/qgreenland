# About

## Create a new `git` branch

Avoid conflicts with other developers!


## Select layers and datasets

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

Specifically examine the whitespace in large strings like `abstract` or
`description` fields. Blank lines may need to be added to compensate for
incorrect YAML in the old format. Compare against the YAML as a guide.

# Run layer migration

Run the following command to create a basic migration of layer(s). Validate
that it looks correct afterwards. Manual changes _WILL_ be required.

`./scripts/cli.sh config-migrate layer {layer_pattern} > config/datasets/{layer}.py`

Specifically examine the whitespace in large strings like `abstract` or
`description` fields. Blank lines may need to be added to compensate for
incorrect YAML in the old format. Compare against the YAML as a guide.
