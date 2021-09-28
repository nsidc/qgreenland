#!/bin/bash
set -e

THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
container_id="$($THIS_DIR/helpers/container_id.sh)"

# If this script is called from Jenkins, docker-compose's default TTY behavior
# will not work. In other situations, we will want the ability to attach to a
# debugger prompt.
if [ -t 1 ]; then
    tty_arg=""
else
    tty_arg="-T"
fi

docker exec -it ${tty_arg} ${container_id} python ./tasks/qgreenland/qgreenland/cli/__init__.py "$@"
