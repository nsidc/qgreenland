#!/bin/bash

set -ex

xhost +

docker run -it \
       -e DISPLAY=$DISPLAY \
       -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
       -v $HOME/.local/share/QGIS/QGIS3/:/root/.local/share/QGIS/QGIS3/:rw \
       -v $PWD/qgis-data/:/root/qgis-data/:rw \
       -v $PWD/luigi/data:/root/data/:rw \
       qgis/qgis:release-3_10 qgis

xhost -
