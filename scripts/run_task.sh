# TODO: --workers=$(nproc)  (or more?)
# Currently hardcoded to 1 because increasing number of workers leads to failures:
#
#    File "/luigi/tasks/qgreenland/util/qgis.py", line 87, in get_map_layer
#        raise RuntimeError(f"Layer located at '{layer_path}' does not exist.")
#        RuntimeError: Layer located at '/luigi/data/luigi-wip/qgreenland/Geophysics/IceBridge BedMachine/bedmachine_bed/bedmachine_bed.tif' does not exist.

# NOTE: Workers must be set to 1 for python debug breakpoints to be usable
docker-compose exec luigi luigi --workers=1 \
  --module qgreenland.tasks.main ZipQGreenland
