#!/bin/bash
set -e

THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
container_id="$($THIS_DIR/helpers/container_id.sh)"

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
    tty_arg="-t"
else
    tty_arg=""
fi

# docker-compose up/down commands are useful for dev, but must be
# removed/commented for prod.
# docker-compose up -d
# NOTE: Workers must be set to 1 for python debug breakpoints to be usable
docker exec -i ${tty_arg} ${container_id} luigi --workers=1 \
  --module qgreenland.tasks.main ZipQGreenland
