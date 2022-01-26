#!/usr/bin/env bash
set -e

if [[ $OSTYPE == 'darwin'* ]]; then
    open_cmd='open'
    watch_cmd='fswatch --batch-marker=EOF -r ./'
else
    open_cmd='xdg-open'
    watch_cmd='inotifywait -e delete -e create -e close_write -r ./'
fi

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/../../doc
HTML_PATH="./_build/html/index.html"

make clean

set +e
make html
$open_cmd "${HTML_PATH}"
set -e

while $watch_cmd; do
    make clean

    set +e
    make html
    set -e
done
