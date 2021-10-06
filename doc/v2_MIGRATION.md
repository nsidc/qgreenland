# About

## Run migration commands

Run the following commands to create a basic migration of a dataset and a
layer. These will need to be manually edited after.

`./scripts/cli.sh config-migrate dataset {dataset_pattern} > config/datasets/{dataset}.py`

`./scripts/cli.sh config-migrate layer {layer_pattern} > config/datasets/{layer}.py`
