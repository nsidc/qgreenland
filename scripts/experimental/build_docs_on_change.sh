#!/usr/bin/env bash
# TODO: How to support OSX?

set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/../../doc
HTML_PATH="./_build/html/index.html"

make clean

set +e
make html
xdg-open "${HTML_PATH}"
set -e

while inotifywait -e delete -e create -e close_write -r ./; do
    make clean

    set +e
    make html
    set -e
done
