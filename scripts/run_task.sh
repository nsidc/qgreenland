# TODO: --workers=$(nproc)  (or more?)
# Currently hardcoded to 1 because increasing number of workers leads to failures:
#
#    File "/luigi/tasks/qgreenland/util/qgis.py", line 87, in get_map_layer
#        raise RuntimeError(f"Layer located at '{layer_path}' does not exist.")
#        RuntimeError: Layer located at '/luigi/data/luigi-wip/qgreenland/Geophysics/IceBridge BedMachine/bedmachine_bed/bedmachine_bed.tif' does not exist.

# If this script is called from Jenkins, docker-compose's default TTY behavior
# will not work. In other situations, we will want the ability to attach to a
# debugger prompt.
if [ -t 1 ]; then
    tty_arg="-T"
else
    tty_arg=""
fi

# NOTE: Workers must be set to 1 for python debug breakpoints to be usable
docker-compose exec ${tty_arg} luigi luigi --workers=1 \
  --module qgreenland.tasks.main ZipQGreenland
