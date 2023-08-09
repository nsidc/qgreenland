# Storage

QGreenland storage locations are currently in the `data/` subdirectory of this
repository. This can be overridden by creating `data/working-storage` and
`data/private-archive` symlinks to your preferred storage locations.

We plan to support storage location overrides using environment variables in
the future.


## Working storage

```
data/working-storage
```

All file outputs of QGreenland are written to working storage. Must be
read-write.


### Dataset fetch storage

```
data/working-storage/fetch-datasets
```

Datasets are fetched from their original locations and written to this
directory.


### WIP storage

```
data/working-storage/wip-layers
data/working-storage/wip-package
```

All intermediate steps are written to these directories.


### Release storage

```
data/working-storage/release-layers
data/working-storage/release-packages
```

Finalized layers and projects are stored in these directories.


## "Private archive" storage

```
data/private-archive
```

While this project prefers to only include publicly-archived and
machine-accessible data, we do have some privately-archived data that we have
sourced by e-mailing scientists or manually interacting with machine-unfriendly
systems. These datasets have an `access_instructions` attribute in configuration
that describes how the data was acquired.

May be read-only.

NOTE: The CLI's `run` command features an argument `--exclude-manual-assets`
flag which will exclude any layers that depend on privately-archived data. It is
recommended to use this flag as a QGreenland contributor testing their changes.
