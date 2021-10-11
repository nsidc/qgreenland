#!/bin/bash
THIS_DIR="$( cd "$(dirname "$0")" || exit 1; pwd -P )"

"$THIS_DIR"/container_cli.sh cleanup "$@"
