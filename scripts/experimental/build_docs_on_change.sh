#!/usr/bin/env bash
set -e

THIS_DIR="$( cd "$(dirname "$0")"; pwd -P )"
cd "$THIS_DIR"/../../doc

make clean && make html || true
while inotifywait -e delete -e create -e close_write -r ./; do
    make clean && make html || true;
done
