#!/usr/bin/env bash
set -e

if [[ $OSTYPE == 'darwin'* ]]; then
    open_cmd='open'
    # NOTE: fswatch exits with 0 even when it receives SIGINT, so you would
    # need to hit CTRL+C a few times to exit
    watch_cmd='fswatch -e '\\.swp$' --event-flags --monitor poll_monitor --one-event --recursive ./'
else
    open_cmd='xdg-open'
    watch_cmd='inotifywait -e delete -e create -e close_write --recursive ./'
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
