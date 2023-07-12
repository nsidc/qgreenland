# QGreenland's `conda` environments

QGreenland has many pieces that require different dependencies, and those are defined in
these different environments.

Environments are defined in `environment.yml` files, and pinned to allow packages to
upgrade over time without too much unexpected breakage. Environments are locked in
`conda-lock.yml` files with exact pins and checksums for reproducibility.


## Locking

In any directory containing an `environment.yml` file, run `conda-lock` to lock that
environment.


## Notes

The `main` and `command` environments are only locked for the `linux-64` platform
because it's expected that they will only be used in a Linux container context.
