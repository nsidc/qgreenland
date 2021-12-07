#!/usr/bin/env bash
set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd $THIS_DIR/../../doc

make clean && make html
while inotifywait -e close_write *; do
    make clean && make html;
done
