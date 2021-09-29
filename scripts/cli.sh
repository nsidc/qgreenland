#!/bin/bash
set -e

if [[ "$1" == "run" || "$1" == "cleanup" ]]; then
    echo "The 'run' and 'cleanup' commands should be run from \`container_cli.sh\`."
    exit 1
fi

THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
cd "$THIS_DIR"/..

python qgreenland/cli/__init__.py "$@"
