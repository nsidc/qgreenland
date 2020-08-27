# v0.33.0 (2020-08-27)

- Start all layer groups as unchecked where possible, and collapsed.
- New "Human activity" layer: GEM research stations
- New "Human activity/Research stations" layer: Seismograph Stations
- New "Background" layer: Ocean shapefile
- New "Geophysics" layer: Geothermal Heat Flux

# v0.32.0 (2020-08-26)

- Use cmocean colormaps:
  - `ice` for sea ice concentration
  - `balance` for ice column thickness change
  - `deep` for bathymetry
- Use colormap from Editorial Board member for vegetation biomass
- New "Environmental Management/Protected Zones" layer: Arctic Protected Areas (CAFF 2017)
- New "Biology/Birds" layer: Thickbilled Murre Colonies (CAFF Arctic Biodiversity Trends 2010)
- New "Biology/Birds" layer: Common Murre Colonies (CAFF Arctic Biodiversity Trends 2010)
- New "Biology/Mammal" layer: Wild Reindeer Populations (CAFF Arctic Biodiversity Trends 2010)
- New "Biology/Fish" layer:  Arctic Char Populations (CAFF)

# v0.31.0 (2020-08-25)

- Add new Hydrology layer: PROMICE land/ice basins, outlets, streams layers.
- Remove Hydrology layer: Hydrologic sub-basins.
- Remove "|" symbol from layer titles.
- Update USGS Earthquakes symbology.
- Update IBCAO Bathymetry symbology (use cmocean "deep" colormap).

# v0.30.0 (2020-08-21)

- Add `project.yml` configuration for project CRS, extents.
  - The "data" extent is focused on Greenland, while the "background" extent
    provides context.
  - Limit extent of most layers to "data" extent.
  - Change Project default extent to "data" extent.
- Add specialized "latlon" style.

# v0.29.0 (2020-08-20)

- Add new Geology & natural resrouces layer: Earthquakes.
- Add new Geology & natural resrouces layer: plate tectonic boundaries.

# v0.28.0 (2020-08-19)

- You no longer require a password to download QGreenland!
- Use `DEFLATE` compression for raster layers instead of `LZW`. `DEFLATE`
  results in a good compromise between the QGreenland zip file size and the
  unziped package size. As of this release:
    - without compression:
      - Unzipped size: 3.7G
      - Zipped size: 631M
    - with `LZW` compression:
      - Unzipped size: 867M
      - Zipped size: 784M
    - with `DEFLATE` compression:
      - Unzipped size: 653M
      - Zipped size: 640M
- Add layer config CSV export utility script
- Add log analysis script: Download and byte count by QGreenland version

# v0.27.0 (2020-08-17)

- Bugfix: layers not requiring earthdata login are no longer downloaded twice.
- Add LZW compression to all raster layers.
- New Oceanography layer: International Bathymetric Chart of the Arctic Ocean
- New Oceanography layer: IHO-IOC GEBCO Gazetteer of Undersea Feature Names

# v0.26.0 (2020-08-12)

- New Miscellaneous layer: Universal Transverse Mercatur (UTM) Zones
- New Miscellaneous layer: Arctic Circle
- New Miscellaneous layers: Latitude and Longitude lines.
- Fix abstract for Permafrost/Ground Ice Conditions layer
- Add scale dependent rendering for glacier IDs and populated places.
- Bugfix: fix UTF encoding errors.
- Renamed 'Ice Sheet Mass Change' layer to 'Ice Column Thickness'
- QGIS project load speedup: remove internal colormap from sea ice concentration
  layers. Use .qml file to style these layers.
- Unscale sea ice concentration layers to percentages. Source GeoTiff files for
  sea ice concentration layers scaled values by 10 so that an internal color map
  could be used (GeoTiff files require integer-based lookup tables for color maps).

# v0.25.0 (2020-08-06)

- Replace `ArcticDEM` layer task with generic `Raster` task.
- Rename `ReprojectRaster` -> `WarpRaster`.
- Add Sea Ice Index layers:
  - Median extent line layers.
  - Sea ice min extent monthly concentrations.
  - Sea ice max extent monthly concentrations.

# v0.24.0 (2020-08-06)

- Re-organize, rename layers and layer groups to spec provided by Twila
- Add BedMachine "sources" from NetCDF datasets to layer descriptions
- Layers are collapsed by default. Previously, layers would be expanded to show
  their entire color maps by default. This took up a significant amount of
  screen space in the table of contents.

# v0.23.0 (2020-08-05)

- Layers now have layer-specific description at the beginning of the tooltip,
  with additional dataset-level information following.
- Add BedMachine Error layer

# v0.22.0 (2020-08-05)

- Add raster layer resolutions in parens after layer title
- Set "Land" layer to invisible so the background layer shows by default
- Move "Arctic DEM" layer above "Land" layer
- Label colormap entries with correct units/descriptions.

# v0.21.0 (2020-08-04)

- Switch to `EPSG:3413` projection: Uses WGS-84 ellipsoid.
- Enable all groups by default
  - This way, everything is one click away -- enabling layers, hiding layers,
    hiding groups. If we want a layer to start invisible, we set that layer to
    invisible, not the group.
- Add new UngzipMany task
- Add GGD602 layer to `Geology & natural resources` layer group.

# v0.20.0 (2020-08-01)

- Add 12.5km Circum-Arctic Map of Permafrost and Ground-Ice Conditions, Version
  2 (https://nsidc.org/data/GGD318/versions/2) layer.

# v0.19.0 (2020-07-30)

- Add ORNL "Circumpolar Arctic Vegetation Biomass layer and style
- Add University of Washington 'Ice-sheet height and thickness changes from
  ICESat to ICESat-2' layer and style

# v0.18.0 (2020-03-18)

- Simplify layer tooltips to only a dataset description.
- New layer: Hydrologic Sub-Basins
- New layer config key: `override_source_projection`
- New layer task: Unrar

# v0.17.0 (2020-03-18)

- New layer: Background image (Natural Earth II 10m).
- New layer: Land shapefile (Natural Earth Land 10m).

# v0.16.0 (2020-03-16)

- New layer: Placenames (Natural Earth Populated Places). Temporarily disabled
  until we can figure out labels.

# v0.15.0 (2020-03-12)

- New layer: Ice Sheet Velocity (500m)
- Preserve final wip layer task output. Previously moved this output to the
  final location.

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
