#!/bin/bash

set -ex

DEST_DIR="/share/appdata/qgreenland/Quantarctica"
URL="data.pgc.umn.edu/gis/packages/quantarctica"
FILE="Quantarctica3.zip"

SRC_URL="${URL}/${FILE}"
DEST_FILE="${DEST_DIR}/${FILE}"

if [ ! -f "${DEST_FILE}" ]; then
  mkdir -p "${DEST_DIR}"
  wget --show-progress "${SRC_URL}" --output-document "${DEST_FILE}"
fi

unzip -o "${DEST_FILE}" -d "${DEST_DIR}"
