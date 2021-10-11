#!/bin/bash
set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"

set +e
container_id="$("$THIS_DIR"/helpers/container_id.sh)"
rc="$?"
set -e
if [ $rc = 1 ]; then
    echo "$container_id"
    exit "$rc"
fi


# If this script is called from Jenkins, docker-compose's default TTY behavior
# will not work. In other situations, we will want the ability to attach to a
# debugger prompt.
if [ -t 1 ]; then
    tty_arg="-t"
else
    tty_arg=""
fi

docker exec -i "${tty_arg}" "${container_id}" python ./tasks/qgreenland/qgreenland/cli/__init__.py "$@"
