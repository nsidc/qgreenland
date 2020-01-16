#!/bin/bash

set -ex

URL="data.pgc.umn.edu/gis/packages/quantarctica"
FILE="Quantarctica3.zip"

if [ ! -f "qgis-data/${FILE}" ]; then
  wget --show-progress "${URL}/${FILE}" --output-document "qgis-data/${FILE}"
fi

unzip -o "qgis-data/${FILE}" -d qgis-data/
