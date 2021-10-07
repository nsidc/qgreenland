#!/bin/bash
set -e

if [[ "$1" == "run" || "$1" == "fetch" || "$1" == "cleanup" ]]; then
    echo "The 'run', 'fetch', and 'cleanup' commands should be run from \`container_cli.sh\`."
    exit 1
fi

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/..

python qgreenland/cli/__init__.py "$@"
