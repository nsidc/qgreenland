#!/usr/bin/env bash
set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/../../doc

make clean && make html
while inotifywait -e modify -e delete -e create -e close_write -r ./; do
    make clean && make html;
done
