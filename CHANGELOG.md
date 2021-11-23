# NEXT_VERSION

- Update clip step in lonlat.py to solve clipping issue on lat layers


# v2.0.0alpha3 (2021-11-23)

- Improved raster compression.
- Convert RACMO promice mask layers to `Byte` data type.
- Update Bedmachine dataset metadata to reflect new v4 data.


# v2.0.0alpha2 (2021-11-22)

- Add scalebar to map viewport in lower-right corner.
- Layer changes:
  - NEW:
    - "Geophysics/Heat flux/Flow from multiple observations (55km)"
    - "Geophysics/Heat flux/Flow measurement locations"
    - "Oceanography/Bathymetry/Depth contours"
    - "Geology/Geological map/Ice thickness contours"
    - "Sea ice/Monthly mean concentration (25 km)/September (min monthly
      extent)/September 2021"
    - "Sea ice/Monthly mean concentration (25 km)/Feb or March (max monthly
      extent)/March 2021"
  - MOVED:
    - "Geophysics/Geothermal heat flux (5km)" layer to "Geophysics/Heat
      flux/Flux from ice cores (Greve, R.) (5km)".
    - "Oceanography/Bathymetric chart of the Arctic Ocean (400m)" layer to
      "Oceanography/Bathymetry/Depth (400m)"
    - "Human activity/Research stations" group to "Human activity/Research
      sites"
  - UPDATED:
    - "Regional climate models/RACMO model output/Runoff 1958-2019 (1km)":
      change colormap, make `0` values transarent.
    - "Reference/Timezones": add labels.
    - "Reference/Borders/Greenland coastlines": update style to remove green
      tint.
    - "Geology/Earthquakes M above 2.5 1900-2020": show all earthquakes in
      background boundary instead of subsetting to region around Greenland.
    - "Reference/Longitude lines": display positive degrees West instead of
      negative.
  - REMOVED from QGreenland zip package; available via QGreenland plugin:
    - "Glaciology/Ice sheet velocity/ITS_LIVE"
    - "Terrain models/Arctic DEM"


# v2.0.0alpha1 (2021-11-03)

- Minimum supported version of QGIS is now `v3.16`.
  - New Time Controller allows visualization of time-series layers.
- Overhaul YAML configuration to Python configuration.
  - All processing steps are now expressed in configuration.
- Add provenance information to QGIS Layer Properties "History" tab.
- Added layers:
  - "Hydrology/Inventory of marginal lakes"
  - "Monthly sea ice extent (1978 - present)" (time-series, online-only)
- Update "Glaciology/Glacier terminus positions 2000-2021" layers to use
  NSIDC-0642 V2 (released Oct. 2021). Add layers for 2017-2021 winter seasons.


# v1.0.2 (2021-02-23)

- Bugfixes for "Sea ice/Weekly age (12.5 km)" layers:
    - Update sea ice age layer titles to correctly reflect the weekly time
      period for each layer. Previously, layer titles indicated a period one day
      longer than it should have been. For example, 'March 26-April 2' should
      have read 'March 26-April 1'.
    - Update sea ice age maximum extent layer for 2010 to use data from April
      2-8 instead of March 26-April 1. This range corresponds to the sea ice
      maximum achieved on April 2.
    - Update sea ice age minimum extent layer for 2015 to use data from February
      19-25 instead of February 12-18. This range corresponds to the sea ice
      maximum achieved on February 25.
    - Update group path for sea ice age layers:
      - "Feb or March (max extent)" -> "Feb, March, or April (max weekly extent)"
      - "September (min extent)" -> "September (min weekly extent)"
- Update sea ice concentration layers group paths for clarity:
  - "Feb or March (max extent)" -> "Feb or March (max monthly extent)"
  - "September (min extent)" -> "September (min monthly extent)"


# v1.0.1 (2021-02-23)

- Remove `STYLE.txt` from zip package.
- Fix README mistakes


# v1.0.0 (2021-02-22)

- Enable Greenland coastline layer by default, add semitransparent fill.
- Avoid use of special characters in layer titles for Windows compatibility.
- Update PDF documentation, add compatibility guide.
- Remove layers due to inaccurate data:
  - All layers in `Biology/Mammals` group
- Update various layer styles.
- Fix various issues in layer/dataset metadata.
- Add notes about data issues to abstracts for various datasets.


# v1.0.0rc2 (2021-02-11)

- Fixed mistake in raster processing code that resulted in GDAL unnecessarily
  requesting ~22GB of diskspace for reprojection.


# v1.0.0rc1 (2021-02-10)

- Add styles for World Magnetic Model layers.
- Fix descriptions for World Magnetic Model layers.
- Increase coverage of Arctic Char and Vegetation Biomass.
- Fix pixel sizes for some rasters.
- Add User Guide and Quick Start Guide pdfs to built package.


# v0.55.0 (2021-02-09)

- Update RACMO data:
 - New version of the Annual mean temperature at 2m 1958-2019 (1km) layer that
   fixes bad temperature values.
- Apply style enhancements to many layers.


# v0.54.0 (2021-02-08)

- Update RACMO data:
  - Mask 1km data with PromiceMask
  - Wind speed and vectors data now use 5.5km resolution source data.
- New "Reference" layers:
  - QGreenland background boundary
  - QGreenland data boundary
- Added compression to all raster layers.
- Only use overviews on largest raster layers.
- Add preliminary styles for several layers.


# v0.53.0 (2021-02-04)

- Update RACMO layers with 2019 data from Brice Noël.
- Populate `{{date_accessed}}` in citation text with modified time of input
  cache dir.
- Update nunagis protected areas layers: convert fields representing unix
  timestamps to dates.
- Layer and group order and names revamped.
- Fixed some vector attribute types, e.g. Populated Places `population` to
  `integer`.
- Removed layers:
  - GLIMS Images
  - Geology / Onshore pattern


# v0.52.0 (2021-01-25)

- Move OpenStreetMap layers into Miscellaneous group.
- All layer groups except Basemaps and Miscellaneous now initialize collapsed
  and unchecked.
- Rename `layer_manifest.csv` -> `layer_list.csv`
- New "Built environment" layers: 
  - Towns and Settlements
  - Comprehensive placenames
- New "Geophysics" layers:
  - Geoid Model
  - Bouguer gravity anomaly
  - Faye (free-air) gravity anomaly
- Add total size of each layer on disk to the `layer_list.csv`


# v0.51.0 (2021-01-12)

- Update private archive datasets to include preprocessing scripts where
  appropriate.
- Fixup issue with ice firn and racmo wind vector layers that had numerical
  fields incorrectly cast to `string`.
- Rename `manifest.csv` -> `layer_manifest.csv`
- Zipped package root directory now reflects the name of the zip file. For
  example, `QGreenland_v1.0.0.zip` will be extracted to a `QGreenland_v1.0.0/`
  directory instead of `qgreenland/`.
- Update GEM research station layer to include full station descriptions (source
  data have truncated descriptions).


# v0.50.0 (2021-01-07)

- New "Sea ice/NSIDC Ice Age (12.5 km)/September (min extent)" layers for each
  week of the annual minimum sea ice extent from 2010-2019.
- New "Sea ice/NSIDC Ice Age (12.5 km)/Feb or March (max extent)" layers for
  each week of the annual maximum sea ice extent from 2010-2019.
- Removed empty layer groups from table of contents.
- Remove "Sea ice/NSIDC Concentration (25 km)/September (min extent)" layer
  for 2009. 2010-2020 represents the latest decade's worth of data.
- Remove "Sea ice/NSIDC Concentration (25 km)/Feb or March (max extent)" layer
  for 2009.2010-2020 represents the latest decade's worth of data.


# v0.49.0 (2021-01-05)

- Remove ocean outline
- Replace "Atmosphere/RACMO model output/5.5km" 'v10m' and 'u10m' layers with
  wind vectors layer, which shows wind speed and direction.



# v0.48.0 (2020-12-18)

- Vector layers are now stored in the Geopackage format instead of as ESRI
  Shapefiles.
- New "Glaciology" layer: Firn Ice Layer Output Thicknesses
- New "Atmosphere/RACMO model output/5.5km" layers:
  - Annual mean wind speed (5.5km)
  - Annual mean wind direction v10m (5.5km)
  - Annual mean wind direction u10m (5.5km)
- New "Atmosphere/RACMO model output/1km" layers:
  - Total Precipitation (1km)
  - Snowfall (1km)
  - Snowmelt (1km)
  - Runoff (1km)
  - Sublimation (1km)
  - Sndiv (Snow drift erosion?) (1km)
  - Annual Mean Temperature at 2m (1km)
- New "Atmosphere/RACMO model output/masks" layers:
  - LAT
  - LON
  - Icemask
  - GrIS
  - GIC
  - Promicemask
  - Topography
  - Grounded Ice
  - Easting
  - Northing


# v0.47.0 (2020-12-17)

- Updated "Glaciology" Mass-balance glacier observation locations (Machguth et al.) layer:
  - Removed entries where no data were found.
  - Layer now has all attributes from the 'overview' tab in the source database.
  - Updated access instructions in dataset configuration.
- New "Terrain models" layer: Danish Map Supply Topographic Map (1:500,000)


# v0.46.0 (2020-12-15)

- New "Biology/Mammals" layers:
  - Caribou Areas
  - Muskoxen Areas
- New "Human activity/Research stations" layers:
  - PROMICE Automated Weather Stations
  - Former PROMICE Automated Weather Stations
  - GC-NET Automated Weather Stations
- New "Glaciology" layer: Mass-balance glacier observation locations (Machguth
  et al.)
- Update "Terrain models" Arctic DEM layer to use 100m resolution source over
  1km.


# v0.45.0 (2020-12-10)

- New "Glaciology/GMB/DTU Space" layers for 2005-2017: Mass Balance Trend.
- New "Geology & natural resources/Mineral and hydrocarbon licenses" layers:
  - Public Licenses
  - Historic Public Licenses


# v0.44.0 (2020-12-09)

- New "Sea ice/NSIDC Concentration (25 km)/September (min extent)" layer: NSIDC Sea Ice Concentration September 2020
- New "Glaciology/Surface elevation change/Observations" layers representing
  Greenland ice sheet surface elevation changes for five year periods between
  1994 and 2019.
- New "Glaciology/Surface elevation change/Errors" layers representing errors in
  the Greenland ice sheet surface elevation changes for five year periods
  between 1994 and 2019.
- New "Glaciology/Ice sheet velocity/CCI" layers:
  - Land Ice Surface Velocity (250m)
  - Land Ice Surface Vertical Velocity (250m)
- ITS_LIVE velocity layers moved to "ITS_LIVE" subgroup under "Glaciology/Ice sheet velocity"


# v0.43.0 (2020-12-08)

- New "Geophysics/World Magnetic Model/202X" layers for each of the main field
  components (D, F, H, I, X, Y, Z) for 2020-2025:
  - SV (secular variation). Secular variation is the slow change in time of the
    main magnetic field.
- Update "Geophysics/World Magnetic Model/202X" layers with more descriptive
  titles.
- "Geophysics/World Magnetic Model" subgroups start collapsed.


# v0.42.0 (2020-12-07)

- "Geophysics/World Magnetic Model" group begins closed.
- New "Geophysics/World Magnetic Model/Dip Pole" layers:
  - Geomagnetic North Dip Pole 2020-2025
  - IGRF Geomagnetic North Dip Pole 1590-2025
- New "Geophysics/World Magnetic Model/Geomagnetic Coordinates (2020)" layers:
  - Geomagnetic North Pole
  - Geomagnetic Latitudes
  - Geomagnetic Longitudes
- Changed map background color from white to gray (rgb[200, 200, 200])


# v0.41.0 (2020-12-04)

- Remove existing "Frozen Ground" layer: Permafrost and Ground-Ice (12.5km). The
  "Frozen Ground" layers provided by the Pangaea Ground Temperature Map replace
  this.
- New "Glaciology/GLIMS" layers:
  - Points
  - Images (points)
  - Polygons
- NSIDC sea ice layers are now clipped to the 'background' boundary instead of
  the immediate rectangular area around Greenland.
- New "Geophysics/World Magnetic Model/202X" layers for 2020-2025:
  - Blackout Zones
  - D (Geomagnetic Declination (Magnetic Variation))
  - F (Total Intensity of the geomagnetic field)
  - H (Horizontal Intensity of the geomagnetic field)
  - X (North Component of the geomagnetic field)
  - Y (East Component of the geomagnetic field)
  - I (Geomagnetic Inclination)
  - Z (Geomagnetic main field down component)


# v0.40.0 (2020-12-02)

- New "Frozen Ground" layers:
  - Ground temperature (10km)
  - Ground temperature standard deviation (10km)
  - Permafrost Probability (10km)
- New "Basemaps" layer: Greenland Coastlines.


# v0.39.0 (2020-12-01)

- New "Glaciology" layer: Sermeq Kujalleq/Jakobshavn Supraglacial Lakes
- Remove "Environmental management/Exclusive economic zones" layer: Exclusive
  Economic Zone
- New "Environmental management/Exclusive economic zones" layers:
  - Exclusive Economic Zone (polyline)
  - Baseline (polyline)
  - 3NM (polyline)
  - 12NM (polyline)
  - 3NM (polygon)
  - Fishing zone (polygon)
- Apply ice mask to ITS_LIVE ice velocity layer.
- New "Glaciology/Ice sheet velocity" layers:
  - Velocity Error
  - Ice mask
- New "Environmental management" layer: NAFO Divisions
- New "Geology & natural resources/Geological map of the Arctic" layers:
  - Onshore pattern
  - Onshore Planar
  - Onshore


# v0.38.0 (2020-11-20)

- New "Environmental management/Exclusive economic zones" layer: Exclusive
  Economic Zone
- Support adding layers from data contained in a private repository (just a
  special directory exposed as a docker volume mount for now).
- Stop displaying dataset abstract and citation information in the layer
  tooltip. This information is still available in each layer's 'Metadata'.
- Add qgreenland.org and qgreenland github URLs in QGreenland's lower-left
  corner citation text.
- Reorder "Basemaps" layers so that land and ocean polygon layers are on top
  of the Natural Earth background image. Disable land and ocean polygons by
  default.
- New "Human Activity" layer: Arctic Sea Routes


# v0.37.0 (2020-11-17)

- New "Biology" layers:
  - Walrus Protected Areas
  - Goose Protected Areas
  - Caribou Calving Areas
  - Beluga Areas
  - Bird Protected Areas
  - Thickbilled Murre Breeding Colony 5km Zones
  - Seabird Breeding Colonies
  - Eider Protected Areas
  - Murre Group 1km Zones
  - Musk Oxen Calving Areas
  - Narwhal Areas
  - Polar Bear Breeding Areas
- New "Built Environment" layers:
  - Municipalities & Population
- New "Environmental Management" layers:
  - UNESCO Treaty Zones
  - No Go Areas
  - Closed Areas
  - Salt or Saline Lake 100m  Zones
  - Homothermic Spring 100m Zones
  - National Park
  - Biological Important Areas in the National Park
  - Nature Protection Areas
- New 'Future projections' layers:
  - Future (year 3007) Ice Sheet coverage - RCP 2.6 Scenario (1.8km)
  - Future (year 3007) Ice Sheet coverage - RCP 4.5 Scenario (1.8km)
  - Future (year 3007) Ice Sheet coverage - RCP 8.5 Scenario (1.8km)
- Removed layers:
  - Wild Reindeer Populations: Data not representative of actual population
    coverage
  - Natural Earth Populated Places: Too much incorrect data - the OSM populated
    places layer is probably more useful
  - Arctic Protected Areas (CAFF 2017): Replaced by more comprehensive NunaGIS
    datasources
- Update GEM research stations symbology to label stations with their names.
- Increase circular background to 40 degrees latitude
- Increase resolution of Natural Earth "Background" layer to 500m


# v0.36.0 (2020-11-09)

- Fix: Remove extraneous `valid.shp` shapefiles from final package.
- Fix: "geothermal heat flux" layer units (MW/m2 -> mW/m2)
- New "Glaciology" layer: Likely Basal Thermal State
- Support for non-rectangular boundaries. Use circular (latitude bounded)
  background boundary.


# v0.35.0 (2020-09-02)

- New files in root of repo:
  - README.txt: A copy of the QGreenland root README
  - CHANGELOG.txt: A copy of this file!
  - CONTRIBUTING.txt: A copy of QGreenland CONTRIBUTING.md
  - manifest.csv: A comma-separated values table of layers and attributes


# v0.34.0 (2020-09-01)

- New online-only "Satellite" layers: Greenland Image Mosaic for 2015 and 2019
- New "Glaciology" layer: Ice Cores
- New "Basemap" layer: countries
- New "Basemap" layer: administrative divisions
- New "Miscellaneous" layer: timezones
- New "Oceanography" layers: World Ocean Atlas (WOA) 2018 temperatures
- Add units suffix to layer styles where appropriate (sea ice concentration,
  geothermal heat flux, earthquakes, vegetation biomass, IBCAO bathymetry)
- Updated style for "Permafrost and Ground-Ice (12.5km)" layer
- Resample BedMachine and IBCAO layers to 500m
- Re-order and style BedMachine to allow stacking display
  - Use cmocean "topo" and "ice" colormaps.
  - Make "0" values transparent for thickness and surface elevation
- Update ocean-related styles:
    - Undersea Feature Names are colored blue rgb(111, 167, 207)
    - Desaturate the ocean background layer color.
    - Add black outline to undersea feature polygons and lines.
- Change Arctic DEM hillshade scale factor from 40 to 5.
- Update UTM Zones with Quantarctica-inspired style including labeling and
  semi-transparency.


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

- Add QGreenland logo and copyright text as QGIS decorations at bottom-left.


# v0.8.0 (2020-02-12)

- Pre-compute statistics for raster layers so that QGIS can render those layers
  with the correct min/max values.


# v0.7.0 (2020-02-11)

- Add task to generate overviews for raster layers.
  - Generate overviews for Arctic DEM layer.

- Add VM configuration and update README on how to use VM to run tasks and serve
  data.


# v0.6.0 (2020-02-07)

- Add citations to each layer as tooltips. We're currently not sure how to
  populate the actual "Abstract" field in the metadata tab in QGIS using
  pyqgis.


# v0.5.0 (2020-02-07)

- Add config option for gdal warp arguments
  - Downsample BedMachine to 1km


# v0.4.0 (2020-02-07)

- New layer: IceBridge BedMachine


# v0.3.0 (2020-02-06)

- Added hillshade style to Arctic DEM layer.


# v0.2.0 (2020-02-05)

- New layer: Arctic DEM


# v0.1.0 (2020-01-23)

- New layer: Coastlines
