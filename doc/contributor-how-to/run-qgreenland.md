# How to run QGreenland

This project uses Docker and `docker-compose` to run each of its components as
services.  See Docker's [Getting started guide](https://docs.docker.com/get-started/).

The docker-compose stack runs Luigi (with visualizer at port 8082) as a service
for running tasks, as well as NGINX (port 80, 443) for hosting outputs.


## How to start the service stack

In order to download data behind Earthdata Login, you must `export` the
following environment variables on the docker host before starting the stack:

* `EARTHDATA_USERNAME`
* `EARTHDATA_PASSWORD`

Developers at NSIDC may use the values stored in Vault at the following path:
`nsidc/apps/qgreenland`. Those outside of NSIDC must use their personal
Earthdata Login credentials. New users to Earthdata can register here:
https://urs.earthdata.nasa.gov/users/new


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


## How to run processing pipelines with the QGreenland CLI

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
input data. See [Assets](/doc/reference/architecture/CONFIGURATION.md#assets)
documentation to learn more about "manual access" assets.

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


### How to debug a Luigi pipeline

Simply add `breakpoint()` anywhere in the pipeline code, then run the pipeline
with 1 worker (the default) and whichever layer(s) you want to debug.
