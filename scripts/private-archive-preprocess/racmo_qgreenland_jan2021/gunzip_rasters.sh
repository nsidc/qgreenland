#!/bin/bash
set -e

DEST_ROOT='/share/appdata/qgreenland-private-archive/racmo_qgreenland_jan2021'

for f in "$DEST_ROOT"/*.gz; do
    # TODO: Omit --keep flag?
    gunzip --keep "$f"
done
