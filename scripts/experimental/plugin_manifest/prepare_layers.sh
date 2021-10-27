#!/bin/bash
# We currently don't write out the layers in the way they need to be organized
# for public hosting.
SRC_DIR='/share/appdata/qgreenland/release/layers'
DEST='./public'

mkdir -p $DEST

cp -R $SRC_DIR/* $DEST/.
