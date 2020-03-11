# v0.14.0 (2020-03-10)

- New layer: Glacier Terminus (nsidc-0642)
- Refactor all configuration files
  - Configure datasets independently of layers
  - Allow specification of ingest task and kwargs in layer configuration
- Automatically generate layer tasks from config -- commenting the config now
  disables pipelines
- Support CMR access by `granule_id` instead of `short_name` and `version`
- Re-order layers so basemaps are below the science data
- Support layer titles in config
- Adjust group names
- Name files after the `layer_id`

# v0.13.0 (2020-02-25)

- Bugfix: Missing constant definitions
- Configure layer and group order based on the position of layers in the
  `layers.yml` config. Groups get created as they are required when adding map
  layers.

# v0.12.0 (2020-02-24)

- Populate metadata fields in layer properties popup with metadata configured in
  layers.yml
- Add `bumpversion` support to project as an invoke task.

# v0.11.0 (2020-02-21)

- Configure the app so that when it runs in production it runs reproducibly by
  cleaning up its intermediate files aggressively.

# v0.10.0 (2020-02-20)

- Move nginx config, Dockerfile & docker-compose.yml to top level.
- Install dependencies from environment-lock.yml
- Move `run_task.sh` and `cleanup.sh` to `scripts/` dir.
- README updates.
- Make layer and layer group visbility configurable.
- Make layer group expand/collapse state configurable.
  - HACK: If the first layer in the legend is in a collapsed layer group, QGIS
    will automatically expand the layer group. Set coastlines layer to be first
    in the legend to avoid this.

# v0.9.0 (2020-02-18)

* Add QGreenland logo and copyright text as QGIS decorations at bottom-left.

# v0.8.0 (2020-02-12)

* Pre-compute statistics for raster layers so that QGIS can render those layers
  with the correct min/max values.

# v0.7.0 (2020-02-11)

* Add task to generate overviews for raster layers.
  * Generate overviews for Arctic DEM layer.

* Add VM configuration and update README on how to use VM to run tasks and serve
  data.

# v0.6.0 (2020-02-07)

* Add citations to each layer as tooltips. We're currently not sure how to
  populate the actual "Abstract" field in the metadata tab in QGIS using
  pyqgis.

# v0.5.0 (2020-02-07)

* Add config option for gdal warp arguments
  * Downsample BedMachine to 1km

# v0.4.0 (2020-02-07)

* New layer: IceBridge BedMachine

# v0.3.0 (2020-02-06)

* Added hillshade style to Arctic DEM layer.

# v0.2.0 (2020-02-05)

* New layer: Arctic DEM

# v0.1.0 (2020-01-23)

* New layer: Coastlines
