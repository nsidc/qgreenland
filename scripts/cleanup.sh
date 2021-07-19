#!/bin/bash

# If this script is called from Jenkins, docker-compose's default TTY behavior
# will not work. In other situations, we will want the ability to attach to a
# debugger prompt.
if [ -t 1 ]; then
    tty_arg=""
else
    tty_arg="-T"
fi

docker-compose exec ${tty_arg} luigi ./tasks/qgreenland/qgreenland/util/cleanup.py "$@"
