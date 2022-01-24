#!/usr/bin/env bash
# TODO: How to support OSX?

set -e

if [[ $OSTYPE == 'darwin'* ]]; then
    open_cmd='open'
    inotify_cmd='fswatch ./'
else
    open_cmd='xdg-open'
    inotify_cmd='inotifywait -e delete -e create -e close_write -r ./'
fi

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/../../doc
HTML_PATH="./_build/html/index.html"

make clean

set +e
make html
$open_cmd "${HTML_PATH}"
set -e

while $inotify_cmd; do
    make clean

    set +e
    make html
    set -e
done
