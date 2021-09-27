#!/bin/bash

THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
cd $THIS_DIR/..

python qgreenland/cli/__init__.py $@
