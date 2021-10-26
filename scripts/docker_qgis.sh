#!/bin/bash
set -ex

xhost +

docker run -it \
       -e DISPLAY="$DISPLAY" \
       -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
       -v "$HOME/.local/share/QGIS/QGIS3/:/root/.local/share/QGIS/QGIS3/:rw" \
       -v /share/appdata/qgreenland/:/data/:rw \
       qgis/qgis:release-3_10 qgis

xhost -
