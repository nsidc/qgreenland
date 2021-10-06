# About

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


# Run layer migration

Run the following command to create a basic migration of layer(s). Validate
that it looks correct afterwards. Manual changes _WILL_ be required.

`./scripts/cli.sh config-migrate layer {layer_pattern} > config/datasets/{layer}.py`
