#!/bin/bash
# We currently don't write out the layers in the way they need to be organized
# for public hosting.
LUIGIDIR='/share/appdata/qgreenland/luigi-wip'
SOURCE="$LUIGIDIR/wip"
DEST='./public'

mkdir -p $DEST

for layer_dir in "$SOURCE"/*; do
    layer_id=$(basename "$layer_dir")
    final_data_dir="$(find "$layer_dir" -maxdepth 1 | sort | tail -n 1)"

    cp -R "$final_data_dir" "$DEST/$layer_id"
done

cp $LUIGIDIR/QGreenland/manifest.json $DEST/.
