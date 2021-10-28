#!/bin/bash
set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"

"$THIS_DIR"/cli.sh cleanup "$@"
