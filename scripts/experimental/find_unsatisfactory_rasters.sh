#!/bin/bash
set -e

# We want to be able to find rasters which don't meet our feature requirements.
# Rasters must be compressed with DEFLATE and contain overviews.

if [ "$1" = "-all" ]; then
    all=1
else
    all=0
fi

QGR_COMPILED_DIR='/share/appdata/qgreenland/luigi-wip/QGreenland'

find "${QGR_COMPILED_DIR}" -name '*.tif' | while read -r r; do
    relative_fp=${r#"$QGR_COMPILED_DIR/"}

    compression=$(gdalinfo -json "$r" | jq '.metadata.IMAGE_STRUCTURE.COMPRESSION');
    set +e
    [[ "$compression" != *"DEFLATE"* ]]
    not_compressed=$?
    set -e

    overviews=$(gdalinfo -json "$r" | jq '.bands[0].overviews | length')
    set  +e
    [[ "$overviews" == "0" ]]
    no_overviews=$?
    set -e

    filesize=$(du -h "$r")

    if (( all == 1)); then
        echo "$relative_fp"
        echo "  Compression: $compression"
        echo "  Overviews: $overviews"
        echo "  Filesize: $filesize"
    else
        if (( not_compressed == 0 || no_overviews == 0 )); then
            echo "$relative_fp"
            if (( not_compressed == 0 )); then
                echo "  Compression type: '$compression'"
            fi

            if (( no_overviews == 0 )); then
                echo "  Overviews missing."
            fi
        fi
    fi
done
